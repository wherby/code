#https://leetcode.com/contest/biweekly-contest-61/ranking 	xi-jun-xiao-zi  


from collections import defaultdict
from functools import lru_cache
from typing import List


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:

        memo = defaultdict(list)
        for start, end, tip in rides:
            memo[start].append((end, tip))

        @lru_cache(None)
        def helper(idx):
            if idx == n:
                return 0
            ans = helper(idx + 1)
            for end, tip in memo[idx]:
                ans = max(ans, end - idx + tip + helper(end))
            return ans

        return helper(1)