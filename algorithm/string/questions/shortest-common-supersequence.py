# https://leetcode.cn/problems/shortest-common-supersequence/submissions/
# https://leetcode.cn/submissions/detail/249540247/  
class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        m,n = len(str1), len(str2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                dp[i][j] = i+j
        for i in range(m):
            for j in range(n):
                
                dp[i+1][j+1] = min(dp[i+1][j] +1, dp[i][j+1] +1)
                if str1[i] == str2[j]:
                    dp[i+1][j+1] = min(dp[i+1][j+1],dp[i][j]+1)
        x,y =m-1,n-1
        mxv = dp[m][n]
        res =""
        while mxv >0:
            print(x,y)
            if str1[x] == str2[y]:
                res += str1[x]
                x -= 1
                y -=1
                mxv -=1
            else:
                if dp[x][y+1]==mxv-1:
                    res += str1[x]
                    x -=1
                    mxv -=1
                else:
                    res += str2[y]
                    y -=1
                    mxv -=1
        #print(dp)
        #print(res[::-1])
        return res[::-1]


re =Solution().shortestCommonSupersequence(str1 = "abac", str2 = "cab")