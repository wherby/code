# https://leetcode.cn/problems/count-substrings-that-differ-by-one-character/
class Solution(object):
    def countSubstrings(self, s, t):
        m,n = len(s),len(t)
        dp,dpr = [[0]*(n+1) for _ in range(m+1)],[[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):           
                dp[i+1][j+1] = dp[i][j] +1 if s[i]==t[j] else 0
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dpr[i][j] = dpr[i+1][j+1]+1 if s[i] == t[j] else 0
        cnt = 0 
        for i in range(m):
            for j in range(n):
                if s[i] != t[j]:
                    cnt += (dp[i][j]+1) * (dpr[i+1][j+1]+1)
        return cnt


re = Solution().countSubstrings(s = "aba", t = "baba")
print(re)