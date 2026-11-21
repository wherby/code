# https://codeforces.com/gym/106797/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/11/1106/solution/cf106797d.md
# algorithm/codeforce/组合题/docs/字符串约束图论和并查集.md
# 二分图约束验证 图形缩点合并(把前缀相同的点合并为一组。验证当前图形是否是二分图)

import init_setting
from cflibs import *
from lib.UnionFind import *


def main():
    n, m = MII()
    us = []
    vs = []
    ts = []

    for _ in range(m):
        u, v, t = MII()
        us.append(u - 1)
        vs.append(v - 1)
        ts.append(t)

    uf = UnionFind(n)

    tmp_path = [[] for _ in range(n)]
    cols = [-1] * n

    st_range = sorted(range(m), key=lambda x: -ts[x])
    l = 0

    ans = 0

    def solve(l, r):
        global ans
        tmp = []

        for i in range(l, r):
            u = us[st_range[i]]
            v = vs[st_range[i]]
            u = uf.find(u)
            v = uf.find(v)

            tmp_path[u].append(v)
            tmp_path[v].append(u)

            tmp.append(u)
            tmp.append(v)

        for u in tmp:
            if cols[u] == -1:
                cols[u] = 0
                que = [u]

                c0 = 0
                c1 = 0

                for u in que:
                    if cols[u] == 0:
                        c0 += uf.getSize(u)
                    else:
                        c1 += uf.getSize(u)

                    for v in tmp_path[u]:
                        if cols[v] == -1:
                            cols[v] = cols[u] ^ 1
                            que.append(v)
                        elif cols[v] == cols[u]:
                            exit(print("impossible"))

                ans += fmin(c0, c1)

        for i in range(l, r):
            u = us[st_range[i]]
            v = vs[st_range[i]]
            uf.merge(u, v)

        for u in tmp:
            cols[u] = -1
            tmp_path[u].clear()

    for i in range(m):
        if ts[st_range[i]] != ts[st_range[l]]:
            solve(l, i)
            l = i

    solve(l, m)
    print("possible")
    print(ans)
