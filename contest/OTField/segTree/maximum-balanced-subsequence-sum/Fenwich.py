from typing import List, Tuple, Optional

from testInput import *

class FenwickTree:
    def __init__(self, n):
        self.bit = [0] * n

    def update(self, idx, x):
        while idx < len(self.bit):
            self.bit[idx] = max(self.bit[idx], x)
            idx |= idx + 1

    def query(self, end):
        x = 0
        while end:
            x = max(x, self.bit[end - 1])
            end &= end - 1
        return x

class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        n = len(nums)
        order = sorted(range(n), key = lambda x: nums[x] - x)
        
        out = max(nums)
        
        seg = FenwickTree(n + 1)
        
        for i in order:
            best = seg.query(i + 1)
            best += nums[i]
            
            out = max(best, out)
            seg.update(i, best)
            
        return out


import time

start = time.time()
re =Solution().maxBalancedSubsequenceSum(nums)
print(re)
end = time.time()
print(end - start)
