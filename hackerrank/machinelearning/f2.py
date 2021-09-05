#https://www.youtube.com/watch?v=JcI5Vnw0b2c&list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v&index=2

import pandas as pd
import quandl
import os

QuandlKey = os.environ["quandlkey"]


df= quandl.get("WIKI/GOOGL", authtoken = QuandlKey)
#print df.head()

df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close'])/df['Adj. Close'] *100.0
df['PCT_Change'] = (df['Adj. Close'] - df['Adj. Open'])/df['Adj. Open'] *100.0
df =df[['Adj. Close','HL_PCT','PCT_Change','Adj. Volume']]

print(df.head)