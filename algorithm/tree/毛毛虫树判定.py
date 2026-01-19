# https://codeforces.com/gym/105242/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0115/solution/cf105242b.md
# 题目需要树是一个特殊的形状，首先树上任何点都最多有3个连接，而且所有3个连接的点都需要在树上构成单链
# 为了证明树上所有三个连接的点都是单链上的点，首先找一个此点做为顶点，然后所有具有三个连接的点都向根的方向运动，然后染色运动方向的路径
# 如果所有点的邻居只有2个被染色，则所有三个交点的点都在同一路径上，这个染色路径就是树的主干



import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        path = [[] for _ in range(n)]
        
        for _ in range(n - 1):
            u, v = GMI()
            path[u].append(v)
            path[v].append(u)
        
        flg = True
        rt = -1
        for i in range(n):
            if len(path[i]) > 3:
                flg = False
            elif len(path[i]) == 3:
                rt = i
        
        if not flg: outs.append('NO')
        elif rt != -1:
            parent = [-1] * n
            que = [rt]
            
            for u in que:
                for v in path[u]:
                    if parent[u] != v:
                        parent[v] = u
                        que.append(v)
            
            vis = [0] * n
            
            for i in range(n):
                if len(path[i]) == 3:
                    cur = i
                    while cur >= 0 and not vis[cur]:
                        vis[cur] = 1
                        cur = parent[cur]
            
            for i in range(n):
                v = 0
                for j in path[i]:
                    v += vis[j]
                if v >= 3: flg = False
            
            outs.append('YES' if flg else 'NO')
            
        else: outs.append('YES')
    
    print('\n'.join(outs))