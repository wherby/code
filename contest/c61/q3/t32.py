#https://leetcode.com/contest/biweekly-contest-61/ranking 1015634
#https://leetcode.com/contest/biweekly-contest-61/problems/maximum-earnings-from-taxi/
# @@@@@!!!!!!!!!!!!!!!!!!!!!!!!!DP....

class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        x = [[] for i in range(n+1)]
        for s, e, t in rides:
            x[e].append((s, t))
        dp = [0 for i in range(n+1)]
        for i in range(1, n+1):
            dp[i] = dp[i-1]
            for s, t in x[i]:
                dp[i] = max(dp[i], dp[s]+i-s+t)
        return dp[n]