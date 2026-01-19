
# https://leetcode.com/contest/biweekly-contest-174/problems/number-of-alternating-xor-partitions/submissions/1887983376/
# 如果用 xor的状态机依次来计算，则 target1 和target2 等于0 的时候，状态很难计算，因为有转移量，所以需要把ndp单独存放，然后返回值是转移量
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
            ndp = [0]*4
            if cur == s[0]:
                ndp[1] += dp[0]

            if cur == s[1]:
                ndp[2] += dp[1]

            if cur == s[2]:
                ndp[3] += dp[2]

            if cur ==s[3]:
                ndp[0] += dp[3]

            dp =[(x+y)%mod for x,y in zip(dp,ndp)]
        return sum(ndp)%mod

re = Solution().alternatingXOR([17218,0],17218,27973)
print(re)