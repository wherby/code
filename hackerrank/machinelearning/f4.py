
import pandas as pd
import quandl
import os
import math
import numpy as np
from sklearn import preprocessing,cross_validation,svm
from sklearn.linear_model import LinearRegression

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
print(forcast_out)

df['label'] = df[forcast_col].shift(-forcast_out)
df.dropna(inplace= True)

X = np.array(df.drop(['label'],1))
y = np.array(df['label'])

X = preprocessing.scale(X)
#X = X[: -forcast_out +1]
#df.dropna(inplace = True)
y = np.array(df['label'])

print(len(X),len(y))

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size =0.2)
#print len(X_train),len(X_test),len(y_train),len(y_test)

clf = LinearRegression()
#clf = svm.SVR()
#clf = svm.SVR(kernel = 'poly')
#clf = LinearRegression(n_jobs = -1)

clf.fit(X_train,y_train)

accuracy=  clf.score(X_test,y_test)

print accuracy
