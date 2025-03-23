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
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        dp =[0]*n
        ps =[0]
        for a in skill:
            ps.append(a + ps[-1])

        for a in mana:
            start = 0
            for i in range(n):
                start = max(start,dp[i]- a*ps[i])
            
            for i in range(n):
                dp[i] = start + ps[i+1]*a
        return dp[-1]





#re =Solution().minTime( skill = [1,5,2,4], mana = [5,1,4,2])
#re =Solution().minTime( skill = [1,2,3,4], mana = [1,2])
re =Solution().minTime( skill = [1,3,4], mana = [2,3,3,3])
print(re)