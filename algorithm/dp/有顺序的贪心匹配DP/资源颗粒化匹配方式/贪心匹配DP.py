# https://leetcode.cn/problems/minimum-total-distance-traveled/description/?envType=daily-question&envId=2026-04-14
# 把factory的资源颗粒化排序
# 虽然题目是DP，但是这里也有贪心的思路，最左的工厂资源可以给最左的robot使用，所以从左到右遍历工厂资源
# 在DP的时候，从右往左遍历robot，确保最左的robot能最先匹配到最左的工厂资源


from typing import List, Tuple, Optional

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        ls = []
        for a,b in factory:
            for _ in range(b):
                ls.append(a)
        ls.sort()
        n = len(robot)
        dp=[10**20]*(n+1)
        dp[0] = 0
        for a in ls:
            for i in range(n,0,-1):
                dp[i] = min(dp[i],dp[i-1] + abs(robot[i-1] - a))
        return dp[-1]


