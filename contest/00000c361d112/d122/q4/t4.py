from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        ret = nums[0]
        nums = nums[1:]
        sl = SortedList([])
        for i in range(dist+1):
            sl.add((nums[i],i))
        def getSum(sl):
            ret = 0 
            for i in range(k-1):
                ret += sl[i][0]
            return ret
        n = len(nums)
        mx = getSum(sl)
        cur = mx
        #print(sl)
        for i in range(dist+1,n):
            l = i-dist-1
            isL =False 
            isI = False
            #print(sl,k)
            if (nums[l],l) <=sl[k-2]:
                cur -= nums[l]
                isL = True
            if (nums[i],i) <=sl[k-2]:
                cur += nums[i]
                isI = True
            sl.add((nums[i],i))
            sl.remove((nums[l],l))
            if isI and not isL:
                cur -= sl[k-1][0]
            if not isI and isL:
                cur += sl[k-2][0]
            mx = min(mx,cur)
        return mx + ret
            





re =Solution().minimumCost(nums = [10,8,18,9], k = 3, dist = 1)
print(re)