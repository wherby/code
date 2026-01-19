# https://leetcode.com/contest/biweekly-contest-174/problems/number-of-alternating-xor-partitions/submissions/1887983376/
# 如果用 xor的状态机依次来计算，则 target1 和target2 等于0 的时候，状态很难计算，因为会有状态重叠
from typing import List, Tuple, Optional



class Solution:
    def alternatingXOR(self, nums: List[int], target1: int, target2: int) -> int:
        # check for t2: t1, t1t2t1=t2
        # check for t1: t1t2, t1t2t1t2=0
        t1 = t1t2 = t1t2t1 = 0
        t1t2t1t2 = 1
        curr = 0
        for n in nums:
            curr ^= n
            dt1 = dt1t2 = dt1t2t1 = dt1t2t1t2 = 0
            if curr == target1:
                dt1 += t1t2t1t2
            if curr ^ target1 == target2:
                dt1t2 += t1
            if curr ^ target1 ^ target2 == target1:
                dt1t2t1 += t1t2
            if curr ^ target2 == target2:
                dt1t2t1t2 += t1t2t1
            t1 += dt1
            t1t2 += dt1t2
            t1t2t1 += dt1t2t1
            t1t2t1t2 += dt1t2t1t2
            # print(curr, t1, t1t2, t1t2t1, t1t2t1t2)
        return (dt1 + dt1t2 + dt1t2t1 + dt1t2t1t2) % 1000000007

re = Solution().alternatingXOR([17218,0],17218,27973)
print(re)