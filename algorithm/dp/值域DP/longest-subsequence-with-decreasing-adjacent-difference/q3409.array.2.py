# https://leetcode.cn/problems/longest-subsequence-with-decreasing-adjacent-difference/description/
from typing import List, Tuple, Optional
from collections import defaultdict,deque
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        mx =max(nums)
        mn =min(nums)
        dp= [[0]*(mx-mn+1) for _ in range(mx+1)]
        for a in nums:
            acc =0
            for j in range(mx-mn,-1,-1):
                if a +j <=mx:
                    acc = max(acc,dp[a+j][j])
                if a -j >=mn:
                    acc = max(acc,dp[a-j][j])
                dp[a][j] = max( acc+1,dp[a][j])
        return max(map(max,dp))

re =Solution().longestSubsequence([6,5,3,4,2,1])
print(re)