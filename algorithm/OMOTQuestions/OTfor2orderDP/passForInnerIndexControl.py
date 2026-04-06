# 12s pass https://leetcode.cn/problems/minimum-operations-to-achieve-at-least-k-peaks/submissions/715288192/
from typing import List, Tuple, Optional
from math import inf

class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:

        n = len(nums)
        if k > n // 2: return -1
        costs = [max(0, max(nums[i-1], nums[(i+1)%n]) + 1 - nums[i]) for i in range(n)]


        def min_cost(arr, k1):
            if k1 <= 0: return 0
            m = len(arr)
            if m < 2 * k1 - 1: return inf
            
            f = [[inf] * 2 for _ in range(k1 + 1)]
            f[0][0] = 0 
            
            for i,c in enumerate(arr):
                new_f = [[inf] * 2 for _ in range(k1 + 1)]
                for j in range(min(k1, i // 2 + 1) + 1):
                    new_f[j][0] = min(f[j][0], f[j][1])
                    if j > 0:
                        new_f[j][1] = f[j-1][0] + c
                f = new_f
                
            return min(f[k1])

        res1 = min_cost(costs[1:], k)
        res2 = costs[0] + min_cost(costs[2:-1], k - 1)
        
        ans = min(res1, res2)
        return ans if ans != inf else -1