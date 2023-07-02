from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        mx = 0
        n = len(nums)
        for i in range(n):
            if nums[i] %2 == 1:continue
            for j in range(i+1,n+1):
                ls = nums[i:j]
                isG = True
                for k,a in enumerate(ls):
                    if a %2 != k%2:
                        isG = False
                    if a > threshold:
                        isG = False
                if isG:
                    mx = max(mx,j-i)
                    #print(ls,mx,j,i)
        return mx

re = Solution().longestAlternatingSubarray(nums = [3,2,5,4], threshold = 5)
print(re)