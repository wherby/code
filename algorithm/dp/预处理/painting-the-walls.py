# https://leetcode.cn/contest/weekly-contest-350/problems/painting-the-walls/
from typing import List, Tuple, Optional

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