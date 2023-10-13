from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        mx = 0
        def verify(mid,idx):
            com= composition[idx]
            acc =0
            for cop,s,c in zip(com,stock,cost):
                 ta = max(0,cop*mid-s)
                 acc += ta*c
            #print(mid,acc)
            return acc <=budget
        for i in range(k):
            l,r = 0,10**9
            while l <r:
                mid = (l+r+1)>>1
                if verify(mid,i):
                    l =mid
                else:
                    r = mid-1
            mx = max(mx,l)
        return mx

            





re =Solution().maxNumberOfAlloys(n = 3, k = 2, budget = 15, composition = [[1,1,1],[1,1,10]], stock = [0,0,100], cost = [1,2,3])
print(re)