# https://nautilustrader.io/docs/latest/getting_started/backtest_high_level
# https://www.histdata.com/download-free-forex-historical-data/?/ascii/tick-data-quotes/

import shutil
from decimal import Decimal
from pathlib import Path

import pandas as pd

from nautilus_trader.backtest.node import BacktestDataConfig
from nautilus_trader.backtest.node import BacktestEngineConfig
from nautilus_trader.backtest.node import BacktestNode
from nautilus_trader.backtest.node import BacktestRunConfig
from nautilus_trader.backtest.node import BacktestVenueConfig
from nautilus_trader.config import ImportableStrategyConfig
from nautilus_trader.core.datetime import dt_to_unix_nanos
from nautilus_trader.model import QuoteTick
from nautilus_trader.persistence.catalog import ParquetDataCatalog
from nautilus_trader.persistence.wranglers import QuoteTickDataWrangler
from nautilus_trader.test_kit.providers import CSVTickDataLoader
from nautilus_trader.test_kit.providers import TestInstrumentProvider


DATA_DIR = "~/Downloads/Data/csv/"

path = Path(DATA_DIR).expanduser()
raw_files = list(path.iterdir())
assert raw_files, f"Unable to find any histdata files in directory {path}"
print(raw_files)

# Here we just take the first data file found and load into a pandas DataFrame
df = CSVTickDataLoader.load(
    file_path=raw_files[0],                                   # Input 1st CSV file
    index_col=0,                                              # Use 1st column in data as index for dataframe
    header=None,                                              # There are no column names in CSV files
    names=["timestamp", "bid_price", "ask_price", "volume"],  # Specify names to individual columns
    usecols=["timestamp", "bid_price", "ask_price"],          # Read only these columns from CSV file into dataframe
    parse_dates=["timestamp"],                                # Specify columns containing date/time
    date_format="%Y%m%d %H%M%S%f",                            # Format for parsing datetime
)

# Let's make sure data are sorted by timestamp
df = df.sort_index()

# Preview of loaded dataframe
print(df.head(2))


# Process quotes using a wrangler
EURUSD = TestInstrumentProvider.default_fx_ccy("EUR/USD")
wrangler = QuoteTickDataWrangler(EURUSD)

ticks = wrangler.process(df)

# Preview: see first 2 ticks
tmp =ticks[0:2]
print(tmp)

CATALOG_PATH = Path.cwd() / "catalog"

# Clear if it already exists, then create fresh
if CATALOG_PATH.exists():
    shutil.rmtree(CATALOG_PATH)
CATALOG_PATH.mkdir(parents=True)

# Create a catalog instance
catalog = ParquetDataCatalog(CATALOG_PATH)

# Write instrument to the catalog
catalog.write_data([EURUSD])

# Write ticks to catalog
catalog.write_data(ticks)


# Get list of all instruments in catalog
catalog.instruments()

# See 1st instrument from catalog
instrument = catalog.instruments()[0]
print(instrument ,"Instrument ")

# Query quote-ticks from catalog
start = dt_to_unix_nanos(pd.Timestamp("2024-10-01", tz="UTC"))
end =  dt_to_unix_nanos(pd.Timestamp("2024-10-15", tz="UTC"))
selected_quote_ticks = catalog.quote_ticks(instrument_ids=[EURUSD.id.value], start=start, end=end)

# Preview first
print(selected_quote_ticks[:2])


venue_configs = [
    BacktestVenueConfig(
        name="SIM",
        oms_type="HEDGING",
        account_type="MARGIN",
        base_currency="USD",
        starting_balances=["1_000_000 USD"],
    ),
]

data_configs = [
    BacktestDataConfig(
        catalog_path=str(CATALOG_PATH),
        data_cls=QuoteTick,
        instrument_id=instrument.id,
        start_time=start,
        end_time=end,
    ),
]

strategies = [
    ImportableStrategyConfig(
        strategy_path="nautilus_trader.examples.strategies.ema_cross:EMACross",
        config_path="nautilus_trader.examples.strategies.ema_cross:EMACrossConfig",
        config={
            "instrument_id": instrument.id,
            "bar_type": "EUR/USD.SIM-15-MINUTE-BID-INTERNAL",
            "fast_ema_period": 10,
            "slow_ema_period": 20,
            "trade_size": Decimal(1_000_000),
        },
    ),
]

config = BacktestRunConfig(
    engine=BacktestEngineConfig(strategies=strategies),
    data=data_configs,
    venues=venue_configs,
)

node = BacktestNode(configs=[config])

results = node.run()
print(results)