# https://leetcode.cn/contest/weekly-contest-421/problems/find-the-number-of-subsequences-with-equal-gcd/submissions/576114206/

from typing import List, Tuple, Optional


from functools import cache

import math


class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        mod = 10**9+7
        n = len(nums)

        @cache
        def dfs(i,x,y):
            if i == n:
                if x == y and x != 0 :
                    return 1
                return 0 
            return (dfs(i+1,x,y) + dfs(i+1,math.gcd(x,nums[i]),y) + dfs(i+1,x,math.gcd(y,nums[i]))) %mod
        return dfs(0,0,0)




re =Solution().subsequencePairCount([1,2,3,4])
print(re)