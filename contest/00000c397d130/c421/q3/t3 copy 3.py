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
    def subsequencePairCount(self, nums: List[int]) -> int:
        mod = 10**9+7
        n = len(nums)

        @cache
        def dfs(i,x,y):
            if i == n:
                if x == y and x != 0 :
                    return 1
                return 0 
            return (dfs(i+1,x,y) + dfs(i+1,math.gcd(x,nums[i]),y) + dfs(i+1,x,math.gcd(y,nums[i]))) %mod
        return dfs(0,0,0)




re =Solution().subsequencePairCount([1,2,3,4])
print(re)