# https://codeforces.com/gym/106728/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0930/solution/cf106728f.md
# 这里不能从1开始正向推最短路问题，因为其他店到达1点的时候，花的时间是最多的，
# 所以应该反向递推，从此点出发时间的“关门时间”是多少，这样就可以反向DP递推所有点的最迟“出发”时间
# 这种“反向 DP / 逆向 Dijkstra”将原本复杂的动态时间限制，巧妙地化解为了具备最优子结构的瓶颈路问题。这种倒推思想在处理带有“截止时间（Deadline）”或“生命周期（Lifespan）”的图论问题中是非常经典且高效的解法！

import init_setting
from cflibs import *
def main():
    n, m = MII()
    
    path = [[] for _ in range(n)]
    
    us = []
    vs = []
    ts = []
    hs = []
    
    for eid in range(m):
        u, v, t, h = MII()
        
        u -= 1
        v -= 1
        
        us.append(u)
        vs.append(v)
        ts.append(t)
        hs.append(h)
        
        path[u].append(eid)
        path[v].append(eid)
    
    inf = 2 * 10 ** 9
    
    latest_time = [-1] * n
    latest_time[0] = inf
    
    def f(x, y):
        return x * n + y
    
    pq = [f(-inf, 0)]
    
    while pq:
        d, u = divmod(heappop(pq), n)
        d = -d
        
        if latest_time[u] == d:
            for eid in path[u]:
                v = us[eid] ^ vs[eid] ^ u
                nd = fmin(d, hs[eid]) - ts[eid]
                
                if nd > latest_time[v]:
                    latest_time[v] = nd
                    heappush(pq, f(-latest_time[v], v))
    
    print(''.join('1' if x >= 0 else '0' for x in latest_time))