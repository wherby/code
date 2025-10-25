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
    def longestBalanced(self, nums: List[int]) -> int:
        n =len(nums)
        mx = 0 
        for i in range(n):
            visit={}
            dp = [0]*2
            for j in range(i,n):
                c = nums[j]
                if c not in visit:
                    visit[c] =1
                    dp[c%2] +=1
                if dp[0] == dp[1]:
                    mx = max(mx,j-i+1)
        return mx




re =Solution().longestBalanced()
print(re)