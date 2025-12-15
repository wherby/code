# https://codeforces.com/gym/106039/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/12/1209/solution/cf106039f.md
# 同一类型的传送，如果直接在图上建立遍历的时候，需要 N**2 次比较(每个接入点的cost不同，导致每个接入点都需要计算)
# 在图中为同一种传送建立虚拟节点，到虚拟节点的cost就是出发点cost，从虚拟点到目的点的cost为0
# 这样就把需要分层计算的图变成了最初的平面图


import init_setting
from cflibs import *
def main(): 
    n, m, k = MII()
    path = [[] for _ in range(n + k)]
    
    for _ in range(m):
        u, v, c = MII()
        u -= 1
        v -= 1
        path[u].append(c * (n + k) + v)
        path[v].append(c * (n + k) + u)
    
    for u in range(n):
        t = II()
        for _ in range(t):
            v, c = MII()
            v = v - 1 + n
            path[u].append(c * (n + k) + v)
            path[v].append(u)
    
    inf = 10 ** 16
    dis = [inf] * (n + k)
    dis[0] = 0
    
    pq = [0]
    while pq:
        d, u = divmod(heappop(pq), n + k)
        if u == n - 1:
            print(d)
            break
        
        if dis[u] == d:
            for msk in path[u]:
                nd, v = divmod(msk, n + k)
                if dis[v] > nd + d:
                    dis[v] = nd + d
                    heappush(pq, dis[v] * (n + k) + v)