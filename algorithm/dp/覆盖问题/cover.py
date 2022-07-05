# https://leetcode.cn/contest/biweekly-contest-74/problems/minimum-white-tiles-after-covering-with-carpets/

#给你一个下标从 0 开始的 二进制 字符串 floor ，它表示地板上砖块的颜色。
#floor[i] = '0' 表示地板上第 i 块砖块的颜色是 黑色 。
#floor[i] = '1' 表示地板上第 i 块砖块的颜色是 白色 。
#同时给你 numCarpets 和 carpetLen 。你有 numCarpets 条 黑色 的地毯，每一条 黑色 的地毯长度都为 carpetLen 块砖块。
# 请你使用这些地毯去覆盖砖块，使得未被覆盖的剩余 白色 砖块的数目 最小 。地毯相互之间可以覆盖。
#请你返回没被覆盖的白色砖块的 最少 数目。

 
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