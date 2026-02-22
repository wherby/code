# 1059M - The Shortest and Longest Path https://codeforces.com/gym/105900/problem/M
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0219/solution/cf105900m.md
# 先求出最短路，然后在最短路的基础上求出最长路, 因为最长路一定在最短路的基础上，所以在求最长路的时候只需要考虑最短路上的边就行了





import init_setting
from cflibs import *
def main(): 
    n, m = MII()
    path = [[] for _ in range(n)]
    
    def f(d, u):
        return d * n + u
    
    for _ in range(m):
        u, v, w = MII()
        u -= 1
        v -= 1
        path[u].append(f(w, v))
    
    inf = 10 ** 12
    
    dis = [inf] * n
    dis[0] = 0
    
    pq = [f(0, 0)]
    
    order = []
    
    while pq:
        d, u = divmod(heappop(pq), n)
        if dis[u] == d:
            order.append(u)
            for msk in path[u]:
                w, v = divmod(msk, n)
                if dis[v] > dis[u] + w:
                    dis[v] = dis[u] + w
                    heappush(pq, f(dis[v], v))
    
    ans = [inf] * n
    ans[0] = 0
    
    for u in order:
        for msk in path[u]:
            w, v = divmod(msk, n)
            if dis[v] == dis[u] + w:
                ans[v] = fmin(ans[v], fmax(ans[u], w))
    
    print(dis[n - 1], ans[n - 1])