# Rotate array
# https://leetcode.cn/problems/collecting-chocolates/
# https://leetcode.cn/circle/discuss/bvOqiS/
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def minCost(self, nums, x):
        ans = sum(nums)
        n = len(nums)
        tmp = nums[:]
        for i in range(n-1):
            tmp = tmp[1:] + [tmp[0]]
            nums = [min(x,y) for x,y in zip(nums,tmp)]
            ans = min(ans,sum(nums) + x*(i+1))
            #@print(mx,acc,i)
        return ans





re =Solution().minCost([31,25,18,59],27)
print(re)