from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        mxl,mnl,mxr =[nums[0]]*n,[nums[0]]*n,[nums[-1]]*n
        for i in range(1,n):
            mxl[i] = max(nums[i],mxl[i-1])
            mxr[n-1-i] = max(nums[n-1-i],mxr[n-i])
        ret = 0
        for i,a in enumerate(nums[1:-1],1):
            ret = max(ret,(mxl[i-1] -a)*mxr[i+1])
        return ret





re =Solution().maximumTripletValue([12,6,1,2,7])
print(re)