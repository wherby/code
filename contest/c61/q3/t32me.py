from collections import defaultdict
class Solution:
    def maxTaxiEarnings(self, n, rides) :
        dp = [0]*(n+1)
        dic =defaultdict(list)
        for s,e,t in rides:
            dic[e].append([s,e,t])
        for i in range(1,n+1):
            dp[i] = dp[i-1]
            for s,e,t in dic[i]:
                dp[i] = max(dp[i], dp[s] + i -s +t)
        return dp[n]


re =Solution().maxTaxiEarnings(10, [[9,10,2],[4,5,6],[6,8,1],[1,5,5],[4,9,5],[1,6,5],[4,8,3],[4,7,10],[1,9,8],[2,3,5]])
print(re)
