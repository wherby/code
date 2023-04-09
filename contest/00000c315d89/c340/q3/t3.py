from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n =len(nums)
        l, r =0, nums[-1]
        def verify(mid):
            cnt =0
            i = 1
            while i<n:
                if nums[i] - nums[i-1]<=mid:
                    cnt +=1 
                    i +=2
                else:
                    i+=1
            return cnt >=p
        #print(l,r)
        while l<r:
            mid = (l+r)>>1
            #print(mid)
            if verify(mid):
                r = mid
            else:
                l = mid+1
        return l
        





re =Solution().minimizeMax(nums = [10,1,2,7,1,3], p = 2)
print(re)