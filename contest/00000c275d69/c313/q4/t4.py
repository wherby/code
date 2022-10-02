def prefix_function(s):
    n = len(s)
    pi = [0]*n
    for i in range(1,n):
        j = pi[i-1]
        while j >0 and s[i] != s[j]:
            j  = pi[j-1]
        if s[i] == s[j]:
            j +=1
        pi[i] = j 
    return pi
class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)
        dp= [[1]*(n+1) for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            s1 =s[i:]
            ps = prefix_function(s1)
            for j,d in enumerate(ps):
                if d*2 == j+1:
                    dp[i][n-1] = max(dp[i][n-1],1 + dp[i+d][n-1])
        return dp[0][n-1] 
            
        



re =Solution().deleteString("abcabcdabc")
print(re)