
# https://codeforces.com/problemset/problem/1938/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/04/0418/solution/cf1938j.md
# 有限制： 不能完全一样的两条路径，先求出一条最短路，再找一个不在路径上的边，求到两个点的最短路即可

from cflibs import *


def main():
    n, m = MII()
    path = [[] for _ in range(n)]

    for _ in range(m):
        u, v, w = MII()
        u -= 1
        v -= 1
        
        path[u].append(w * n + v)
        path[v].append(w * n + u)

    parent = [-1] * n

    inf = 10 ** 9

    dis1 = [inf] * n
    dis1[0] = 0

    pq = [0]

    while pq:
        d, u = divmod(heappop(pq), n)
        if dis1[u] == d:
            for msk in path[u]:
                w, v = divmod(msk, n)
                if d + w < dis1[v]:
                    dis1[v] = d + w
                    parent[v] = u
                    heappush(pq, dis1[v] * n + v)

    vis = [0] * n
    cur = n - 1

    vis[cur] = 1

    while parent[cur] != -1:
        cur = parent[cur]
        vis[cur] = 1

    disn = [inf] * n
    disn[n - 1] = 0

    pq = [n - 1]

    while pq:
        d, u = divmod(heappop(pq), n)
        if disn[u] == d:
            for msk in path[u]:
                w, v = divmod(msk, n)
                if d + w < disn[v]:
                    disn[v] = d + w
                    parent[v] = u
                    heappush(pq, disn[v] * n + v)

    ans = inf

    for u in range(n):
        for msk in path[u]:
            w, v = divmod(msk, n)
            if vis[u] and vis[v] and (parent[u] == v or parent[v] == u):
                continue
            ans = fmin(ans, dis1[u] + disn[v] + w)

    print(ans + dis1[n - 1] if ans < inf else -1)