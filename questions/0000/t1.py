import heapq

def getNumber(index):
    primes = [3,5,7]
    hp = [3]
    heapq.heappush(hp, 5)
    heapq.heappush(hp, 7)
    dic ={}
    res =0
    cnt = 0
    while cnt < index:
        res = heapq.heappop(hp)
        cnt +=1
        #print("aa : ", res)
        for i in primes:
            t2 = res * i
            #print(t2)
            if t2 not in dic:
                dic[t2] =1
                heapq.heappush(hp, t2)
        #print(hp)
    return res

for i in range(400):
    print(getNumber(i))

