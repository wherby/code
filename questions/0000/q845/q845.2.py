# https://leetcode.cn/problems/k-similar-strings/submissions/
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        s,t = [],[]
        for x,y in zip(s1,s2):
            if x != y :
                s.append(x)
                t.append(y)
        n = len(s)
        if n ==0 :
            return 0 
        ans = n-1
        def dfs(i,cost):
            nonlocal ans 
            if cost> ans:
                return
            while i < n and s[i] ==t[i]:
                i+=1
            if i ==n:
                ans = min(ans,cost)
                return
            diff = sum(s[j] != t[j] for j in range(i,n))
            if cost + (diff +1)//2 >= ans:  ## 剪枝
                return
            for j in range(i+1,n):
                if s[j] ==t[i]:
                    s[i],s[j] = s[j],s[i]
                    dfs(i+1,cost+1)
                    s[i],s[j] = s[j],s[i]
        dfs(0,0)
        return ans

re = Solution().kSimilarity(s1 = "abc", s2 = "bca")
print(re)