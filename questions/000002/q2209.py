# https://leetcode.cn/problems/minimum-white-tiles-after-covering-with-carpets/submissions/286094576/?envType=daily-question&envId=2025-02-21

class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        dp= [[0]*(n+1) for _ in range(numCarpets +1)]
        for i in range(1,n+1):
            dp[0][i] = dp[0][i-1] + (floor[i-1] == "1")
        
        for i in range(1,numCarpets+1):
            pre = 0
            for j in range(1,n+1):
                if j <=carpetLen:
                    dp[i][j]  = dp[i-1][0]
                else:
                    dp[i][j] = min(dp[i-1][j-carpetLen],pre + (floor[j-1] =="1"))
                    pre = dp[i][j]
            #print(dp)
        return dp[-1][-1]


re = Solution().minimumWhiteTiles(floor = "11111", numCarpets = 2, carpetLen = 3)
print(re)