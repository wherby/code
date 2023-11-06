class Solution:
    def firstDayBeenInAllRooms(self, nextVisit) :
        n = len(nextVisit)
        dp = [0] *n
        sm = [0] *n
        CNST = 10**9 +7
        for i in range(1,n):
            dp[i] =(sm[i-1] -sm[nextVisit[i-1]] + 2)% CNST
            sm[i]= (sm[i-1] + dp[i])%CNST
        #print(dp,sm)
        return sm[-1]




nextVisit = [0,0,2]
re = Solution().firstDayBeenInAllRooms(nextVisit)
print(re)