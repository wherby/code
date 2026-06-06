# https://codeforces.com/gym/106552/problem/I
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0604/solution/cf106552i.md
# 使用人和语言分别代表图中的点，利用关系建图，因为语言的种类比较少
# 分别枚举从语言出发到各自的人的路径最短长度
# 利用其中路径等于两边长度/2 -1的关系计算最短路径


import init_setting
from cflibs import *
def main():
    n, m, q = MII()
    path = [[] for _ in range(n + m)]
    
    for u in range(n):
        _, *idxs = GMI()
        
        for v in idxs:
            path[u].append(n + v)
            path[n + v].append(u)
    
    dis = [[-1] * (n + m) for _ in range(m)]
    
    for x in range(m):
        que = [n + x]
        dis[x][n + x] = 0
        
        for u in que:
            for v in path[u]:
                if dis[x][v] == -1:
                    dis[x][v] = dis[x][u] + 1
                    que.append(v)
    
    outs = []
    inf = 100000
    
    for _ in range(q):
        u, v = GMI()
        ans = inf
        
        for x in range(m):
            if dis[x][u] != -1 and dis[x][v] != -1:
                ans = fmin(ans, dis[x][u] + dis[x][v])
        
        outs.append(ans // 2 - 1 if ans < inf else -1)
    
    print('\n'.join(map(str, outs)))