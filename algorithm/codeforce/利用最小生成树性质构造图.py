# https://codeforces.com/problemset/problem/605/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/05/0508/solution/cf605b.md
# 最小生成树的性质，构造冗余边的约束
from cflibs import *
def main():
    n, m = MII()

    vals = []
    bs = []

    for _ in range(m):
        v, b = MII()
        vals.append(v)
        bs.append(b)

    st_range = sorted(range(m), key=lambda x: vals[x] * 2 + 1 - bs[x])

    us = [-1] * m
    vs = [-1] * m

    cur = 2

    u = 2
    v = 1

    for eid in st_range:
        if bs[eid]:
            us[eid] = 1
            vs[eid] = cur
            cur += 1
        else:
            v += 1
            if v == u:
                u += 1
                v = 2
            if u >= cur:
                exit(print(-1))
            else:
                us[eid] = u
                vs[eid] = v

    print('\n'.join(f'{us[i]} {vs[i]}' for i in range(m)))