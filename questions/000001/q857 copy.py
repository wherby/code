from typing import List, Tuple, Optional
from heapq import heapify,heappop,heappush,heapreplace,heappushpop
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        ls = sorted([(q,w) for q,w in zip(quality,wage)],key= lambda qw:qw[1]/qw[0])
        st = []
        acc= 0
        n = len(ls)
        for i in range(k):
            acc += ls[i][0]
            heappush(st,(-ls[i][0],ls[i][1]))
        ret = acc * ls[k-1][1]/ls[k-1][0]
        #print(ls,ret)
        for i in range(k,n):
            q,w = ls[i]
            #print(st[0][0],q,acc)
            if q <-st[0][0]:
                acc += q + st[0][0]
                heapreplace(st,(-q,w))
                ret = min(ret,w/q *acc)
                #print(st,acc)
            #print(ret,acc,q,w)
        return ret
        
        
re =Solution().mincostToHireWorkers(quality = [10,20,5], wage = [70,50,30], k = 2)
print(re)