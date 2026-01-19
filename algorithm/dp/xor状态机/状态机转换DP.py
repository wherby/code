# https://leetcode.com/contest/biweekly-contest-174/problems/number-of-alternating-xor-partitions/
from typing import List, Tuple, Optional
from collections import defaultdict,deque
class Solution:
    def alternatingXOR(self, nums: List[int], target1: int, target2: int) -> int:
        mod = 10**9+7
        cur = 0
        state1 = defaultdict(int )
        state2 = defaultdict(int)
        state2[0] = 1
        for a in nums:
            cur = cur^a 
            dp1 = state2[cur^target1]
            dp2 = state1[cur^target2]
            state1[cur] = (state1[cur] + dp1)%mod 
            state2[cur] = (state2[cur] + dp2)%mod 
        return (dp1 + dp2) %mod