# https://codeforces.com/problemset/problem/1423/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/04/0428/solution/cf1423b.md
from cflibs import *

def main():
    n, m = MII()

    us = []
    vs = []
    ds = []

    for _ in range(m):
        u, v, d = MII()
        u -= 1
        v -= 1
        us.append(u)
        vs.append(v)
        ds.append(d)

    tmp = sorted(ds)

    l, r = 0, m - 1

    while l <= r:
        mid = (l + r) // 2

        deadline = tmp[mid]

        path = [[] for _ in range(n)]
        
        for i in range(m):
            if ds[i] <= deadline:
                path[us[i]].append(vs[i])
        
        match1, match2 = hopcroft_karp(path, n, n)
        if -1 in match1: l = mid + 1
        else: r = mid - 1

    print(tmp[l] if l < m else -1)