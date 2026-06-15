# https://leetcode.cn/contest/weekly-contest-505/problems/maximum-sum-of-m-non-overlapping-subarrays-i/
# 在最内层用单调栈维护了最大值，把三维变二维， 而最大值的求取是子数组和，与两个index有关，所以拆分index,把与target有关的部分拆分出去

from typing import List, Tuple, Optional
from collections import deque

class Solution:
    def maximumSum(self, nums: List[int], m: int, l: int, r: int) -> int:
        n = len(nums)
        pre = [0]
        for a in nums:
            pre.append(pre[-1]+a)
        dp = [[-10**20]*(m+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 0 
        ans = sum(nums[:l])

        for j in range(1,m+1):
            q= deque()

            for i in range(1,n+1):
                dp[i][j] = dp[i-1][j]
                target = i -l 
                if target>=0:
                    val = dp[target][j-1] - pre[target]
                    while q and (dp[q[-1]][j-1] - pre[q[-1]]) <= val:
                        q.pop()
                    q.append(target)
                if q and q[0]< i-r:
                    q.popleft()
                if q:
                    t = q[0]
                    cur = pre[i] + (dp[t][j-1] - pre[t])
                    dp[i][j] = max(dp[i][j],cur)
                ans = max(ans,dp[i][j])
        return ans