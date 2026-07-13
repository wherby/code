# https://leetcode.cn/contest/weekly-contest-509/problems/subsequence-after-one-replacement/description/

class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        
        def search(s,t):
            dp = [0]*n 
            cur = 0
            for i in range(n):
                if cur < m and   t[i] == s[cur]:
                    cur +=1 
                dp[i] = cur
            return dp
        dp1 = [0]+search(s,t)+[0]
        dp2 = [0]+search(s[::-1],t[::-1])[::-1] +[0]
        for i in range(1,n+1):
            if dp1[i] >=m or dp2[i]>=m:
                return True
            if dp1[i-1] + dp2[i+1]+1 >= m :
                return True
        
        return False