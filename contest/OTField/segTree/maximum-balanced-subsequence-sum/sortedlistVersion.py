from typing import List, Tuple, Optional
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf

from testInput import *



class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        mx = 0
        if max(nums)<0:
            return max(nums)
        sl= SortedList([(-10**10,0)])
        for i,a in enumerate(nums):
            if a <=0:continue
            t= a-i 
            k = sl.bisect_left((t,10**30))
            tt=sl[k-1][1] +a 
            rm = []
            for i in range(k,len(sl)):
                if tt>= sl[i][1]:
                    rm.append(sl[i])
            for a in rm:
                sl.remove(a)
            sl.add((t,tt))
            mx = max(mx,sl[-1][1])
            #print(sl,tt,t)
        return mx

import time

start = time.time()
re =Solution().maxBalancedSubsequenceSum(nums)
print(re)
end = time.time()
print(end - start)
