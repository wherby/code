# https://codeforces.com/gym/105501/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0417/solution/cf105501g.md
# 由于每个点只有一个出度，所以是一个基环树 
# algorithm/graph/基环树/基环内向树森林求最大独立集.md
# 使用反图使得内基环树 变成外基环，这样才能把环上树的值反向计算回到环上，然后环上DP 拆成链计算 algorithm/dp/环DP/index.md
# 这个题目GEMINI会理解错误？



import init_setting
from cflibs import *
def main():
    n = II()
    graph = LGMI()
    
    rev_graph = [[] for _ in range(n)]
    for i in range(n):
        rev_graph[graph[i]].append(i)
    
    indeg = [0] * n
    for x in graph:
        indeg[x] += 1
    
    stk = [i for i in range(n) if indeg[i] == 0]
    while stk:
        u = stk.pop()
        indeg[graph[u]] -= 1
        if indeg[graph[u]] == 0:
            stk.append(graph[u])
    
    vis = [0] * n
    
    dp0 = [0] * n
    dp1 = [0] * n
    
    ans = 0
    
    for i in range(n):
        if indeg[i] and not vis[i]:
            cycle = [i]
            vis[i] = 1
            
            while graph[cycle[-1]] != i:
                cycle.append(graph[cycle[-1]])
                vis[cycle[-1]] = 1
            
            v0s = []
            v1s = []
            
            for u in cycle:
                que = [u]
                for x in que:
                    for y in rev_graph[x]:
                        if not vis[y]:
                            vis[y] = 1
                            que.append(y)
                
                for x in reversed(que):
                    dp1[x] = 1
                    for y in rev_graph[x]:
                        if indeg[y] == 0:
                            dp0[x] += fmax(dp0[y], dp1[y])
                            dp1[x] += dp0[y]
    
                v0s.append(dp0[u])
                v1s.append(dp1[u])
            
            k = len(v0s)
            res = 0
            
            val0 = 0
            val1 = 0
            
            for i in range(1, k):
                val0, val1 = fmax(val0, val1) + v0s[i], val0 + v1s[i]
            
            res = fmax(res, v0s[0] + fmax(val0, val1))
    
            val0 = 0
            val1 = 0
            
            for i in range(k - 1):
                val0, val1 = fmax(val0, val1) + v0s[i], val0 + v1s[i]
            
            res = fmax(res, v0s[-1] + fmax(val0, val1))
            
            ans += res
    
    print(n - ans)