from typing import List, Tuple, Optional

 

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        jobs = jobDifficulty
        if len(jobDifficulty) < d:
            return -1
        n = len(jobDifficulty)
        dp = [[10**9]*(n) for _ in range(d) ]
        dp[0][-1]=0
        for i in range(n):
            dp[0][i] = max(dp[0][i-1],jobs[i])
        for i in range(1,d):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j-1] + jobs[j]
                mx = jobs[j]
                for k in range(j-1,i-2,-1):
                    mx = max(mx, jobs[k])
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + mx)
        #print(dp)
        return dp[-1][-1]

        




re = Solution().minDifficulty(jobDifficulty = [11,111,22,222,33,333,44,444], d = 6)
print(re)