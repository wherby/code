from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        c = len(set(nums))
        sm = 0
        n =len(nums)
        for i in range(n):
            dic = {}
            for j in range(i,n):
                dic[nums[j]] =1 
                if len(dic.keys()) ==c:
                    sm +=1
        return sm





re =Solution()
print(re)