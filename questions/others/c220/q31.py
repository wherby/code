# TDK DP using queue to record max value.
import collections
class Solution(object):
    def maxResult(self, nums, k):
        n = len(nums)
        dp =[-10**9] *n
        dp[0] = nums[0]

        q = collections.deque([0])
        for i in range(1,n):
            while q and q[0] < i-k:
                q.popleft()
            dp[i] = dp[q[0]] + nums[i]
            while q and dp[i] > dp[q[-1]]:
                q.pop()
            q.append(i)
        return dp[-1]