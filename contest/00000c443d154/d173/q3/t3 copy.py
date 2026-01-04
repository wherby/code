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
from itertools import pairwise
class Solution:
    def findMaxVal(self, n: int, restrictions: List[List[int]], diff: List[int]) -> int:
        dp = [10**10]*n 
        dp[0] = 0 
        for idx,val in restrictions:
            dp[idx]  = val 
        
        for i in range(n-1):
            dp[i+1] = min(dp[i+1],dp[i]+diff[i])
        #print(dp)
        for i in range(n-2,-1,-1):
            dp[i] = min(dp[i],dp[i+1]+diff[i])
        #print(dp)
        for i in range(n-1):
            if dp[i+1]> dp[i] + diff[i]:
                dp[i+1] = dp[i]+diff[i]
        return max(dp)






re =Solution().findMaxVal(n = 3, restrictions = [[2,1],[1,3]], diff = [4,1])
#re =Solution().findMaxVal(n = 2, restrictions = [[1,15]], diff = [2])
print(re)