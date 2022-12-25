# https://leetcode.cn/problems/minimum-adjacent-swaps-for-k-consecutive-ones/
# https://www.youtube.com/watch?v=Il5sSd-AReI&ab_channel=HuifengGuan

from typing import List, Tuple, Optional
import math
class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        g, preSum = [], [0]
        for i, num in enumerate(nums):
            if num == 1:
                g.append(i - len(g))
                preSum.append(preSum[-1] + g[-1])
        m, res = len(g), math.inf
        for i in range(m - k + 1):
            mid = i + k // 2
            r = g[mid]
            res = min(res, (1 - k % 2) * r + (preSum[i + k] - preSum[mid + 1]) - (preSum[mid] - preSum[i]))
        return res