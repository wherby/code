# https://codeforces.com/gym/106531/problem/H
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/05/0519/solution/cf106531h.md
# 拓扑排序的时候，利用DP维护了最先访问该点的时间
# 使用排序的invalid 来更新最新可访问时间




import init_setting
from cflibs import *
def main():  
    n, m = MII()
    
    path = [[] for _ in range(n)]
    indeg = [0] * n
    
    for _ in range(m):
        u, v = GMI()
        path[u].append(v)
        indeg[v] += 1
    
    k = II()
    invalid_notes = [[] for _ in range(n)]
    
    for i in range(k):
        j, x = MII()
        invalid_notes[x - 1].append(j)
    
    dp = [1] * n
    
    vis = [0] * n
    stk = [i for i in range(n) if indeg[i] == 0]
    
    while stk:
        u = stk.pop()
        vis[u] = 1
        
        invalid_notes[u].sort()
        for x in invalid_notes[u]:
            if dp[u] == x:
                dp[u] += 1
        
        for v in path[u]:
            indeg[v] -= 1
            dp[v] = fmax(dp[v], dp[u] + 1)
            
            if indeg[v] == 0:
                stk.append(v)
    
    print(max(dp) if sum(vis) == n else -1)