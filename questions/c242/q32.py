class Solution(object):
    def canReach(self, s, minJump, maxJump):
        n = len(s)
        dp =[0]*n
        pre = [0]*n
        pre[0]=1

        for i in range(1,n):
            if s[i] =="0" and (pre[i-minJump] -pre[i-maxJump -1] >0):
                dp[i] =1
            pre[i] = pre[i-1] + dp[i]
        #print(dp,pre)
        return dp[n-1] ==1

re = Solution().canReach("011010",2,3)
print(re)