#https://leetcode.cn/contest/biweekly-contest-99/problems/count-number-of-possible-root-nodes/
#  https://github.com/EndlessCheng/codeforces-go/blob/master/copypasta/dp.go#L2607
# https://www.bilibili.com/video/BV1dY4y1C77x/?spm_id_from=333.999.0.0
# https://leetcode.cn/circle/discuss/xxeFPk/

from typing import List


class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        g = [[] for _ in range(len(edges)+1)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        sg = {(x,y) for x,y in guesses}
        
        def dfs(x,p):
            res = 0
            res += (p,x) in sg
            for a in g[x]:
                if a != p :
                    res += dfs(a,x)
            return res
        cnt0 = dfs(0,-1)
        #print(cnt0)
        ans = 0
        def reRoot(x,y,cnt):
            nonlocal ans
            if cnt >=k:
                ans +=1
            for a in g[x]:
                if a != y:
                    ## change the root from x,to y and recalc the new value
                    reRoot(a,x,cnt - ((x,a) in sg ) +((a,x) in sg))  
        reRoot(0,-1,cnt0)
        return ans
        
        
re =Solution().rootCount(edges = [[0,1],[1,2],[2,3],[3,4]], guesses = [[1,0],[3,4],[2,1],[3,2]], k = 1)
print(re)