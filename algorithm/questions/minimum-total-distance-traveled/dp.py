# https://leetcode.cn/contest/weekly-contest-318/problems/minimum-total-distance-traveled/
from typing import List
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        m = len(robot)
        dp = [10**20 for _ in range(m+1)]
        dp[0]= 0
        for p,n in factory:  ## 消耗品在外层循环
            for _ in range(n):
                for i in range(m,0,-1):  ## 反向，确定消耗品只能计算一次
                    d = abs(p-robot[i-1])
                    dp[i] = min(dp[i],dp[i-1] +d)
        return dp[-1]        
        