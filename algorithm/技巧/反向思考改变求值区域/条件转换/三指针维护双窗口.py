# https://leetcode.cn/problems/count-subarrays-with-k-distinct-integers/description/
from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf
from collections import defaultdict

class Solution:
    def countSubarrays(self, nums: list[int], k: int, m: int) -> int:
        n = len(nums)
        ans = 0
        c = defaultdict(int)
        kn = 0 
        l = 0
        l2 = 0
        

        c2 = defaultdict(int)
        kn2 = 0

        for i in range(n):
            x = nums[i]

            c[x] += 1
            if c[x] == m: kn += 1
            

            c2[x] += 1
            if c2[x] == m: kn2 += 1
            
            while len(c) > k:
                out = nums[l]
                if c[out] == m: kn -= 1
                c[out] -= 1
                if c[out] == 0: del c[out]
                l += 1
            
            while l2 < l:
                out2 = nums[l2]
                if c2[out2] == m: kn2 -= 1
                c2[out2] -= 1
                if c2[out2] == 0: del c2[out2]
                l2 += 1
            
            while l2 < i:
                target = nums[l2]
                if c2[target] > m:
                    c2[target] -= 1
                    l2 += 1
                elif len(c2) > k:
                    if c2[target] == m: kn2 -= 1
                    c2[target] -= 1
                    if c2[target] == 0: del c2[target]
                    l2 += 1
                else:
                    break
            
            if len(c) == k and kn == k:
                ans += (l2 - l + 1)
        
        return ans
            





re =Solution().countSubarrays( nums = [1,2,1,2,2], k = 2, m = 2)
print(re)