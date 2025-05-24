# https://codeforces.com/problemset/problem/1915/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/05/0519/solution/cf1915g.md
# 
# 记录每个节点的可能状态为msk， Dijkstra 用 dist数组 在入栈的时候标记 标记最小值
from cflibs import *
def main():
    t = II()
    outs = []

    inf = 10 ** 12

    for _ in range(t):
        n, m = MII()
        path = [[] for _ in range(n)]
        
        for _ in range(m):
            u, v, w = MII()
            u -= 1
            v -= 1
            
            path[u].append(w * n + v)
            path[v].append(w * n + u)
        
        bikes = LII()

        def f(dist, pos, bike):
            return (dist * n + pos) * n + bike
        
        dis = [inf] * (n * n)
        
        dis[0] = 0
        pq = [f(0, 0, 0)]
        
        while pq:
            d, msk = divmod(heappop(pq), n * n)
            if dis[msk] == d:
                u, b = divmod(msk, n)
                
                for e_msk in path[u]:
                    w, v = divmod(e_msk, n)
                    
                    nd = d + w * bikes[b]
                    nb = b if bikes[b] <= bikes[v] else v
                    
                    nmsk = v * n + nb
                    
                    if dis[nmsk] > nd:
                        dis[nmsk] = nd
                        heappush(pq, f(nd, v, nb))
        
        outs.append(min(dis[(n - 1) * n + j] for j in range(n)))

    print('\n'.join(map(str, outs)))