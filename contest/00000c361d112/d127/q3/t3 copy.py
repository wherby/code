from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l,r = 1,n
        if max(nums)>=k:
            return 1 
        acc = 0
        for a in nums:
            acc |=a 
        if acc <k:
            return -1

        pls = [[0]*32 ]
        for a in nums:
            acc = list(pls[-1])
            for i in range(32):
                if a &(1<<i):
                    acc[i] +=1
            pls.append(acc)
        #print(pls)
        def getN(acc):
            sm = 0
            for i in range(32):
                if acc[i]>0:
                    sm += 1<<i
            return sm
        def verify(mid):
            for i in range(mid,n+1):
                acc = [b-a for b,a in zip(pls[i],pls[i-mid])]
                if getN(acc) >=k:
                    return True
            return False
            
        while l < r:
            mid = (l+r)>>1
            if not verify(mid):
                l = mid +1
            else:
                r = mid
        return l if verify(l) else -1





re =Solution().minimumSubarrayLength(nums = [2,1,8], k = 12)
print(re)