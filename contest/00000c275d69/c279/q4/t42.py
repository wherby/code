class Solution(object):
    def minimumTime(self, s):
        n = len(s)
        ans = n
        dp =[0]*n
        for i in range(n):
            if s[i] =="1":
                dp[i] = min(i+1,dp[i-1]+2)
            else:
                dp[i] = min(i,dp[i-1])
        #print(dp)
        for i in range(n):
            ans = min(ans,dp[i] + n-i-1)
        return ans
        
re = Solution().minimumTime("111000000111000000111")
print(re)