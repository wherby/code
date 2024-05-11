from typing import List, Tuple, Optional
from heapq import heapify,heappop,heappush,heapreplace,heappushpop
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        ls = sorted([(q,w) for q,w in zip(quality,wage)],key= lambda qw:qw[1]/qw[0])
        st = []
        ret = 10**29
        acc= 0
        n = len(ls)
        for i in range(k-1):
            acc += ls[i][0]
            heappush(st,(-ls[i][0],ls[i][1]))
        for i in range(k-1,n):
            q,w = ls[i]
            #print(q,w,i-k+1,i)
            acc += q 
            ret = min(ret,w/q *acc)
            heappush(st,(-ls[i][0],ls[i][1]))
            q1,w1= heappop(st)
            acc +=q1
            #print(ret,acc,q,w)
        return ret
        
        
re =Solution().mincostToHireWorkers(quality = [10,20,5], wage = [70,50,30], k = 2)
print(re)