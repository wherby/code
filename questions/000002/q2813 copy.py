from typing import List, Tuple, Optional
from heapq import heapify,heappop,heappush 
class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(reverse= True)
        cand = []
        dic ={}
        sm =0
        n = len(items)
        m = 0
        for i in range(n):
            a= items[i]
            if a[1] not in dic and m < k:
                dic[tuple(a +[i])] =1
                dic[a[1]] =1
                m+=1
                heappush(cand,a)
        for i,a in enumerate(items):
            if len(cand) <k and tuple(a+[i]) not in dic:
                heappush(cand,a)
                dic[tuple(a+[i])] =1

        for i,a in  enumerate(items):
            if tuple(a+[i]) not in dic:
                h1 = cand[0][0]
                
                if a[0] -h1 -(m**2-(m-1)**2)>=0:
                    m -= 1 
                    heappop(cand)
                    heappush(cand, a)
        for a in cand:
            sm +=a[0]

        return sm + m**2
    


re =Solution().findMaximumElegance([[2,2],[2,2]],2)
print(re)