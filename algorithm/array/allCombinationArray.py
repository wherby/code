# https://leetcode.cn/contest/biweekly-contest-104/problems/power-of-heroes/
# https://leetcode.cn/circle/discuss/OMJd2e/
from typing import List, Tuple, Optional

class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        nums.sort()
        ret = 0
        b = 0
        mod = 10**9+7
        for i, a in enumerate(nums):
            ret += a*a *(b+a)
            b = b*2+a
            b,ret = b%mod,ret %mod
        return ret