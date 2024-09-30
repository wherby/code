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
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        dp = [[0]*n for _ in range(2)]
        dp[0][0],dp[1][0] = energyDrinkA[0],energyDrinkB[0]
        ls = [energyDrinkA,energyDrinkB]
        for i in range(1,n):
            for j in range(2):
                dp[j][i] = max(dp[j][i-1] +ls[j][i], dp[1-j][i-1] )
        return max(dp[0][-1],dp[1][-1])





re =Solution().maxEnergyBoost(energyDrinkA = [4,1,1], energyDrinkB = [1,1,3])
print(re)