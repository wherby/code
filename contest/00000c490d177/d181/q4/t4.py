# https://leetcode.cn/contest/biweekly-contest-181/problems/k-th-smallest-remaining-even-integer-in-subarray-queries/description/
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



class Solution:
    def kthRemainingInteger(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i+1] = pre[i] + (1 if nums[i] % 2 == 0 else 0)
        
        ans = []
        
        for a,b,k in queries:
            l = 1
            r = k  + 10**6
            re = -1
            while l <= r:
                mid = (l + r) // 2
                tar = 2 * mid
                idx = bisect_right(nums, tar, a, b + 1) - 1
                removed = 0
                if idx >= a:
                    removed = pre[idx + 1] - pre[a]
                remaining = mid - removed
                
                if remaining >=k:
                    re = mid
                    r = mid - 1
                else:
                    l = mid +1
            
            ans.append(re*2)
        return ans 



re =Solution().kthRemainingInteger(nums = [1,4,7], queries = [[0,2,1],[1,1,2],[0,0,3]])
print(re)