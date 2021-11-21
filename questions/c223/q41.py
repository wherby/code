# Timeout for python
class Solution(object):
    def minimumTimeRequired(self, jobs, k):
        """
        :type jobs: List[int]
        :type k: int
        :rtype: int
        """
        MX = 10**20
        dp= [[0]*4096 for _ in range(13)]
        n = len(jobs)
        costState = [0]*4096
        for i in range(4096):
            ret =0
            for j in range(n):
                if i & (1<<j) !=0:
                    ret += jobs[j]
            costState[i] = ret 
        for i in range(1,4096):
            dp[0][i] = MX
        dp[0][0] =0

        for i in range(1,k+1):
            for state in range(1<<n):
                subset = state
                dp[i][state] =MX
                while subset>0:
                    dp[i][state] =min(dp[i][state],max(dp[i-1][state-subset],costState[subset]))
                    subset = (subset)-1 &state
        #print(k,n,dp[2][:40],costState[:40])
        return dp[k][(1<<n) -1]


j=[256,250,255,250,254,255,260,260,250,252,257,253]
k=9
re = Solution().minimumTimeRequired(j, k )
print(re)
                