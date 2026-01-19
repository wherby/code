
# https://leetcode.com/contest/biweekly-contest-174/problems/number-of-alternating-xor-partitions/submissions/1887983376/
# 如果用 xor的状态机依次来计算，则 target1 和target2 等于0 的时候，状态很难计算，
from typing import List, Tuple, Optional

class Solution:
    def alternatingXOR(self, nums: List[int], target1: int, target2: int) -> int:
        mod = 10**9+7
        cur = 0
        dp=[0]*4
        dp[0] = 1 
        s = [target1,target1^target2,target2,0]
        for a in nums:
            cur = cur ^a 
            if cur == s[0]:
                dp[1] += dp[0]
            if cur == s[1]:
                dp[2] += dp[1]
            if cur == s[2]:
                dp[3] += dp[2]
            if cur ==s[3]:
                dp[0] += dp[3]
            dp = [b%mod for b in dp]
        if cur == s[0]:
            return dp[1]
        elif cur == s[1]:
            return dp[2]
        elif cur == s[2]:
            return dp[3]
        elif cur == s[3]:
            return (dp[0] -1 )%mod 
        return 0

re = Solution().alternatingXOR([17218,0],17218,27973)
print(re)