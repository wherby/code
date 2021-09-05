
import pandas as pd
import quandl
import os
import math,datetime
import numpy as np
from sklearn import preprocessing,cross_validation,svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

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



X = np.array(df.drop(['label'],1))
#print X[:10]
X = preprocessing.scale(X)
#print X[:10]
X = X[:-forcast_out]
x_lately = X[-forcast_out:]



df.dropna(inplace= True)
#print df.tail()
y = np.array(df['label'])


X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size =0.2)


clf = LinearRegression()
clf.fit(X_train,y_train)
accuracy=  clf.score(X_test,y_test)

#print accuracy

forcast_set = clf.predict(x_lately)
print(forcast_set, accuracy, forcast_out)

df['Forecast'] = np.nan
last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix +one_day

for i in forcast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns) -1)] +[i]
#print df.tail()

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

