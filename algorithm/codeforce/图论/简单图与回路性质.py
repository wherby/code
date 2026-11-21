# https://codeforces.com/gym/106353/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/11/1114/solution/cf106353c.md
# 就是在树上加上边，然后保持加上的边，使得树上形成回路，
# 由于回路的性质决定了树上的边取值是固定的，所以用逆BFS序就能唯一确定每条边是否在回路里

import init_setting
from cflibs import *


def main():
    n = II()
    path = [[] for _ in range(n)]

    for _ in range(n - 1):
        u, v, w = MII()
        u -= 1
        v -= 1
        path[u].append(w * n + v)
        path[v].append(w * n + u)

    parent = [-1] * n
    que = [0]

    for u in que:
        for msk in path[u]:
            w, v = divmod(msk, n)

            if u == 0 or parent[u] % n != v:
                parent[v] = w * n + u
                que.append(v)

    sz = [0] * n

    m = II()

    for _ in range(m):
        u, v = GMI()
        sz[u] ^= 1
        sz[v] ^= 1

    ans = 0

    for u in reversed(que):
        if u:
            w, p = divmod(parent[u], n)
            sz[p] ^= sz[u]
            ans += sz[u] * w

    print(ans)
