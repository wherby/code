# https://leetcode-cn.com/contest/season/2022-spring/problems/ZbAuEH/
# m => 90 will timeout m => 50 will pass for python
class Solution(object):
    def getMaximumNumber(self, moles):
        """
        :type moles: List[List[int]]
        :rtype: int
        """
        moles.append([0,1,1])
        moles.sort()
        n = len(moles)
        dp = [-10**8]*n
        dp[0] =0
        mx =0
        m = 90
        for i in range(1,n):
            for j in range(1,m):
                if i -j <0:continue
                k = i-j
                dt  =moles[i][0] -moles[k][0]
                dis = abs(moles[i][1] -moles[k][1]) + abs(moles[i][2] -moles[k][2])
                if dt>=dis:
                    dp[i] = max(dp[i],dp[k]+1)
                #print(dt,dis,j,i)
            mx = max(dp[i],mx)
        #print(dp)
        return mx

re = Solution().getMaximumNumber( moles = [[1,1,0],[2,0,1],[4,2,2]])
print(re)