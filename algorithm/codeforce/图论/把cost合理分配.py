# https://codeforces.com/gym/106575/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0623/solution/cf106575b.md
# 这里cost 是两条路径的cost, 把它分配到进入的路径cost， 出去的路径为0就可以用最短路径法
# 而且两个Block的路径是不通的


import init_setting
from cflibs import *
def main():
    n, m, k, c = MII()
    blocked = [0] * n
    
    for x in GMI():
        blocked[x] = 1
    
    cost = LII()
    
    path = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v = GMI()
        
        if blocked[u] and blocked[v]: continue
        
        w = 0
        
        if blocked[u]: w = cost[u]
        if blocked[v]: w = cost[v]
        
        path[u].append(w * n + v)
        path[v].append(w * n + u)
    
    dis = [2 * c + 5] * n
    
    dis[0] = 0
    pq = [0]
    
    while pq:
        d, u = divmod(heappop(pq), n)
        
        if dis[u] == d:
            for msk in path[u]:
                w, v = divmod(msk, n)
                if d + w < dis[v]:
                    dis[v] = d + w
                    heappush(pq, dis[v] * n + v)
    
    print(dis[n - 1] // 2 if dis[n - 1] <= 2 * c else -1)