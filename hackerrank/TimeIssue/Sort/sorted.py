from timeit import default_timer as timer
import random
w = [random.randint(0,1999999) for i in range(100000) ]
#w =range(1000000)
start = timer()
index = [i[0] for i in sorted(enumerate(w), key=lambda x:x[1])]
res =[]
for i in range(100):
    res.append(w[index[i]])
print res
end = timer()
print(end - start)

start = timer()
w.sort(key= lambda x:x ,reverse =False)
print w[:100]
end = timer()
print(end - start)