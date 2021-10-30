import heapq
def getNumber(index):
    primes = [3,5,7]
    hp = [3,5,7]
    dic ={}
    res =0
    cnt = 0
    mx =0
    while cnt < index:
        res = heapq.heappop(hp)
        cnt +=1
        for i in primes:
            t2 = res * i
            if t2 not in dic:
                dic[t2] =1
                heapq.heappush(hp, t2)
        mx = max(mx,len(hp))
    return (res,mx)




for i in range(1000):
    print(getNumber(i))