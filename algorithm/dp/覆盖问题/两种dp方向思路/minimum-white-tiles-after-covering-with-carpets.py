# https://leetcode.cn/problems/minimum-white-tiles-after-covering-with-carpets/submissions/601568175/?envType=daily-question&envId=2025-02-21

class Solution:
    def minimumWhiteTiles(self, floor: str, num: int, carpetLen: int) -> int:
        n = len(floor)
        dp = [[0]*(num+1) for _ in range(n+1)]
        for i in range(n):
            dp[i][0] += dp[i-1][0] +(floor[i] =="1")
            if i+1 >=carpetLen:
                for j in range(1,num+1):
                    dp[i][j] = min(dp[i-1][j] + (floor[i] =="1"),dp[i-carpetLen][j-1])
       # print(dp)
        return min(dp[n-1])