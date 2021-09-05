import numpy as np 
from math import sqrt
import warnings
from collections import Counter
import pandas as pd 
import random


def k_nearest_neighbors(data, predict, k =3):
    if len(data) >=k:
        warnings.warn('k is set to value less than totoal voting groups')
    distances = []
    for group in data:
        for features in data[group]:
            #euclidean_distance = np.sqrt(np.sum((np.array(features) - np.array(predict)) **2))
            euclidean_distance = np.linalg.norm(np.array(features) - np.array(predict))
            distances.append([euclidean_distance, group])
    votes = [ i[1]  for  i in sorted(distances)[:k]]
    #print(sorted(distances))
    #print( Counter(votes).most_common(1))
    vote_result = Counter(votes).most_common(1)[0][0]
    confidence =  Counter(votes).most_common(1)[0][1] *1.0 /k

    #print (vote_result, confidence)
    return vote_result,confidence



df = pd.read_csv('breast-cancer-wisconsion.data')
df.replace('?', -99999, inplace =True)
df.drop(['id'] , 1, inplace = True)
full_data = df.astype(float).values.tolist()
#print(full_data[:10])

random.shuffle(full_data)
#print(full_data[:10])

test_size = 0.2

train_set = {2:[], 4:[]}
test_set = {2:[], 4:[]}
train_data = full_data[:-int(test_size *len(full_data))]
test_data = full_data[int(test_size *len(full_data)):]

for i in train_data:
    train_set[i[-1]].append(i[:-1])

for i in test_data:
    test_set[i[-1]].append(i[:-1])

correct  = 0.0
total = 0 
accuracies =[]
for i in range(3,15):
    for group in test_set:
        for data in test_set[group]:
            vote,confidence = k_nearest_neighbors(train_set,data, k =i)
            if group == vote:
                correct += 1
            else:
                #print confidence
                pass
            total +=1

    print(i," :","Accuracy: ", correct /total)
    accuracies.append(correct/total)
print accuracies