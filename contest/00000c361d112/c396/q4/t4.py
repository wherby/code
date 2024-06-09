from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf

class Solution:
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        sm = sum(nums)
        n = len(nums)
        mx = max(nums)
        mod = 10**9+7
        rest =  (mx*n -sm)
        if cost1*2<=cost2:
            return (mx*n -sm)*cost1 %mod
        ls = sorted([mx-a for a in nums], reverse= True)
        ret = rest * cost1
        #print(ls,rest)
        if ls[0]*2 >= rest:
            ret = (ls[0] - (rest-ls[0]))*cost1 + (rest-ls[0])*cost2
            #print(ret)
            r1 = ls[0] - (rest-ls[0])
            if n !=2:
                m1 = r1 //(n-2)
                ret = min(ret,(rest-ls[0])*cost2 +m1*(n-1)*cost2 + (r1- (n-2)*m1)*cost1)
                r2 = r1- (n-2)*m1
                if r2 != 0:
                    ret = min(ret,((mx+ m1+1)*n-sm)//2 *cost2 + ((mx+ m1+1)*n-sm)%2 *cost1)
                    if ((mx+ m1+1)*n-sm)%2 and (n-2)%2 == 1:
                        ret = min(ret,((mx+ m1+2)*n-sm)//2*cost2)
            #print("a")
        else:
            ret = min(ret,rest//2*cost2 + rest%2 *cost1)
            #print(ret, rest%2)
            if n>2 and rest%2 and (n-2)%2 ==1:
                ret =min(ret,(rest + n)//2 *cost2)
        return ret%mod




re =Solution().minCostToEqualizeArray([4,29,63,29,33],8,3)
print(re)