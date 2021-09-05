
import pandas as pd
import quandl
import os
import math

QuandlKey = os.environ["quandlkey"]


df= quandl.get("WIKI/GOOGL", authtoken = QuandlKey)
#print df.head()

df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close'])/df['Adj. Close'] *100.0
df['PCT_Change'] = (df['Adj. Close'] - df['Adj. Open'])/df['Adj. Open'] *100.0
df =df[['Adj. Close','HL_PCT','PCT_Change','Adj. Volume']]

forcast_col = "Adj. Close"
df.fillna(-9999,inplace= True)

forcast_out = int(math.ceil(0.01 * len(df)))

df['label'] = df[forcast_col].shift(-forcast_out)
df.dropna(inplace= True)

print df.head()
print df.tail()