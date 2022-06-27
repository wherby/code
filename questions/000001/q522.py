class Solution:
    def findLUSlength(self, strs) -> int:
        def lcs(s1,s2):
            m,n = len(s1),len(s2)
            dp=[[0]*(n+1) for _ in range(m+1)]
            for i in range(1,m+1):
                for j in range(1,n+1):
                    a1,a2 = s1[i-1],s2[j-1]
                    if a1 ==a2:
                        dp[i][j] = dp[i-1][j-1] +1
                    else:
                        dp[i][j] = max(dp[i][j-1],dp[i-1][j])
            return dp[m][n]
        ret = []
        n = len(strs)
        for i in range(n):
            fd = False
            for j in range(n):
                if i ==j:
                    continue
                if lcs(strs[i],strs[j]) == min(len(strs[i]),len(strs[j])):
                    fd = True
                    break
            if fd == False:
                ret.append(strs[i])
        if len(ret) ==0:
            return -1
        else:
            k = max(map(lambda x: len(x),ret))
            n = len([x for x in ret if len(x) ==k ])
            return n 
        
re =Solution().findLUSlength(["aaa","aaa","aa"])
print(re)