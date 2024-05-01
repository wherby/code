from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
class Solution:
    def totalCost(self, cs: List[int], k: int, m: int) -> int:
        sm= 0 
        st1,st2=[],[]
        visit = {}
        n = len(cs)
        idx1,idx2 = m,n-1-m
        for i in range(m):
            heapq.heappush(st1,(cs[i],i))
            heapq.heappush(st2,(cs[n-1-i],n-1-i))
        for _ in range(k):
            #print(st1,st2,visit)
            while st1 and  st1[0][1] in visit:
                heapq.heappop(st1)
                #print(st1,st2,len(visit),idx1,idx2)
            while st2 and st2[0][1] in visit:
                heapq.heappop(st2)
            if st1 and st1[0] <st2[0]:
                a,idx = heapq.heappop(st1)
                visit[idx] =1
                sm +=a 
                if idx1 < n:
                    heapq.heappush(st1,(cs[idx1],idx1))
                idx1 +=1
            else:
                a,idx = heapq.heappop(st2)
                visit[idx] =1
                sm +=a 
                if idx2 >=0:
                    heapq.heappush(st2,(cs[idx2],idx2))
                idx2 -=1
        return sm

re = Solution().totalCost([25,65,41,31,14,20,59,42,43,57,73,45,30,77,17,38,20,11,17,65,55,85,74,32,84],24,8)
print(re)