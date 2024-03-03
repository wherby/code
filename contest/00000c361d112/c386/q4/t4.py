from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf

class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n = len(changeIndices)
        m = len(nums)
        l,r = m,n+1
        def verify(mid):
            ls = changeIndices[:mid]
            visit={}
            cnum = list(nums)
            acc = 0 
            for a in ls[::-1]:
                a = a-1
                if a in visit or acc ==0:
                    acc +=1
                elif cnum[a]>0:
                    cnum[a] =0
                    acc -=1
                    visit[a] =1
                else:
                    acc +=1
            sm1 = sum(cnum)
            #print(mid,sm1,cnum,acc,visit)
            return acc >= sm1 + m - len(visit)
            
        
        while l<r:
            mid = (l+r)>>1
            #print(mid,verify(mid))
            if not verify(mid):
                l = mid +1
            else:
                r = mid 
        return l if l <=n else -1
            
        
        




re =Solution().earliestSecondToMarkIndices([5,3,2,0,3,5],[4,3,6,5,6,5,3,6,4,1,2,3,6,1])
print(re)