from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        left =0
        n  =len(nums)
        acc =0
        dic = defaultdict(int)
        for i,a in enumerate(nums):
            dic[a] +=1
            inc = 0
            while max(dic.keys())-min(dic.keys())>2:
                b = nums[left]
                dic[b] -=1
                left +=1
                if dic[b] ==0:
                    del dic[b]
            acc += i-left +1
        return acc





re =Solution().continuousSubarrays([5,4,2,4])
print(re)