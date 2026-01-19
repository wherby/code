# https://leetcode.cn/problems/find-the-minimum-amount-of-time-to-brew-potions/submissions/?envType=daily-question&envId=2025-10-09
# 需要手写max解决超时问题
# 第一次遍历找到dp[i]的左约束，得到最右值的确定值，第2次遍历利用最右值确定前面值的约束
# 左右约束两次遍历
from typing import List, Tuple, Optional

class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        dp = [0]*(n+1) 

        for b in mana:
            acc = 0 
            for i,a in enumerate(skill):
                acc +=a 
                dp[i] = (dp[i] if dp[i]>dp[i-1] else dp[i-1])  + a*b   #max(dp[i] + a*b, dp[i-1]+ a*b)
            for i in range(n-2,-1,-1):
                dp[i] = dp[i+1] - b*skill[i+1]
        return dp[n-1]

