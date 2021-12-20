class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        mx,path,n = 1,set(),len(s)
        def dfs(idx):
            nonlocal mx
            if idx ==n:
                mx = max(mx,len(path))
                return
            if n -idx +len(path) <= mx: return
            tmp= ''
            for i in range(idx,n):
                tmp += s[i]
                if tmp not in path:
                    path.add(tmp)
                    dfs(i+1)
                    path.remove(tmp)
        dfs(0)
        return mx
re =Solution().maxUniqueSplit("ababccc")
print(re)