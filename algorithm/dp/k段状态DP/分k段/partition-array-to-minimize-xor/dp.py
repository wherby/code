# https://leetcode.cn/contest/weekly-contest-456/problems/partition-array-to-minimize-xor/description/
from typing import List, Tuple, Optional


fmax = lambda x, y: x if x > y else y
fmin = lambda x, y: x if x < y else y
class Solution:
    def minXor(self, nums: List[int], k: int) -> int:
        pre = [0]
        for a in nums:
            pre.append(a^pre[-1])
        n = len(nums)
        dp = [[10**20]*(k+1) for _ in range(n+1)]
        dp[0][0] = 0 
        for i in range(1,n+1):
            for k1 in range(1,k+1):
                for j in range(k1-1,i):
                    dp[i][k1] = fmin(dp[i][k1],fmax(dp[j][k1-1], pre[i] ^ pre[j]))
        return dp[n][k]


re =Solution().minXor( nums = [2,3,3,2,4]*50, k = 150)
print(re)