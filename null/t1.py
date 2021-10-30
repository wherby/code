#[] >0
#prime [3,5,7]
#3,5,7,9,15,21,27,25,35 
import heapq
def getNum(index):
    cnt =0
    hp =[]
    seed = [1]
    prime=[3,5,7]
    res =0
    dic ={}
    dic2={}
    mn =7
    while cnt != index:
        newseed =[]
        for s in seed:
            for p in prime:
                t = s*p
                if t > mn*7:
                    newseed.append(s)
                else:
                    if t not in dic2:
                        dic2[t]=1
                        newseed.append(t)
                        heapq.heappush(hp,t)
        t = hp[0]
        if t not in dic:
            cnt +=1
            res = heapq.heappop(hp)
            dic[res]=1
        else:
            heapq.heappop(hp)
        seed = newseed
        #print(hp)
        mn = res
    return res

arr= [1,2,3]
for i in range(1,500):
    re = getNum(i)
    print(re)


