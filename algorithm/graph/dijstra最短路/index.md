




## 
最短路的时候，在入栈的时候需要更新最短路的值
https://leetcode.cn/problems/minimum-cost-path-with-edge-reversals/submissions/?envType=daily-question&envId=2026-01-27
```Python
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        rg = [[] for _ in range(n)]
        for a,b,c in edges:
            g[a].append((b,c))
            g[b].append((a,c*2))
        visit =[10**10]*n
        st = [(0,0)]
        while st:
            cost,a = heappop(st)
            if visit[a] <cost :
                continue 
            visit[a] = cost 
            if a == n-1:
                return cost
            for b,c in g[a]:
                if visit[b] > cost +c: 
                    visit[b] = cost+c
                    heappush(st,(cost+c,b))

        return -1
```