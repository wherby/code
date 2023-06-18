from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        for i in range(n):
            time[i] +=1
        dp = [10**10]*(n+1)
        dp[0] = 0
        for i in range(n):
            a = time[i]
            for j in range(n,-1,-1):
                if j <=a:
                    dp[j] =min(dp[j],cost[i])
                else:
                    dp[j] = min(dp[j],dp[j-a]+ cost[i])
        
        return dp[n]
        



re =Solution().paintWalls([42,8,28,35,21,13,21,35],[2,1,1,1,2,1,1,2])
print(re== 63)
re =Solution().paintWalls([26,53,10,24,25,20,63,51],[1,1,1,1,2,2,2,1])
print(re==55)