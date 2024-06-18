from typing import List, Tuple, Optional
from heapq import heapify,heappop,heappush 
class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(reverse= True)
        cand = []
        dic ={}
        sm =0
        for i in range(k):
            if items[i][1] not in dic:
                dic[items[i][1]] =1 
                sm += items[i][0]
            else:
                heappush(cand,items[i])
        n = len(items)
        for i in range(k,n):
            if items[i][1] not in dic and cand:
                k1 = len(dic)
                t1 = cand[0][0]
                if (k1+1)**2 -(t1-items[i][0])>=0:
                    dic[items[i][1]] =1 
                    cand.pop()
                    sm += items[i][0]
        for a in cand:
            sm += a[0]
        return sm + len(dic)**2
    


re =Solution().findMaximumElegance(items = [[3,1],[3,1],[2,2],[5,3]], k = 3)
print(re)