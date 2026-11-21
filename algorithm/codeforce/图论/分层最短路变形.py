# https://codeforces.com/gym/106788/problem/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/11/1104/solution/cf106788j.md
# 这个题目看起来像是分层最短路，但是路径的最小K值是变化的，分层就不可以
# 这里看起来要做二分找到最小第K值的选择，但是这里的函数不是单调函数，二分不行，且取值不是连续的，三分也不是很好
# algorithm/codeforce/图论/docs/什么情况下可以使用二分三分.md

import init_setting
from cflibs import *


def main():
    n, m, k = MII()
    inf = 10**9

    path = [[] for _ in range(n)]
    ws = []

    for _ in range(m):
        u, v, w = MII()
        path[u].append(w * n + v)
        ws.append(w)

    ans = inf

    for w0 in ws:
        dis = [inf] * n
        dis[0] = 0

        pq = [0]
        while pq:
            d, u = divmod(heappop(pq), n)

            if dis[u] == d:
                for msk in path[u]:
                    w, v = divmod(msk, n)
                    nd = d + fmax(w, w0)

                    if nd < dis[v]:
                        dis[v] = nd
                        heappush(pq, dis[v] * n + v)

        ans = fmin(ans, dis[n - 1] - w0 * k)

    print(fmax(ans, 0))
