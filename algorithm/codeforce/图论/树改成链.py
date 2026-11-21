# https://codeforces.com/gym/106356/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/11/1112/solution/cf106356c.md
# 其实这里的思路就是找到下一个节点，把它连接到此节点，因为是此节点的bfs查找，所以路径中的节点不会是已经遍历过的节点了
# 同时每次遍历的时候，把路径变成了菊花型。使得下次遍历的时候更快
# 这里path remove 操作可能耗时比较多，变成set可能更好

import init_setting
from cflibs import *


def main():
    t = II()
    outs = []

    for _ in range(t):
        n = II()
        p = LII()

        path = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u, v = MII()
            path[u].append(v)
            path[v].append(u)

        ops = []

        for i in range(n - 1):
            rt = p[i]
            parent = [-1] * (n + 1)

            que = [rt]

            for u in que:
                for v in path[u]:
                    if parent[u] != v:
                        parent[v] = u
                        que.append(v)

            a = p[i + 1]
            b = parent[a]

            path[a].remove(b)
            path[b].remove(a)

            while b != rt:
                ops.append(f"{a} {b} {parent[b]}")
                b = parent[b]

            path[a].append(rt)
            path[rt].append(a)

        outs.append(f"{len(ops)}")
        if ops:
            outs.append("\n".join(ops))

    print("\n".join(outs))
