# https://codeforces.com/problemset/problem/260/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/06/0626/solution/cf260d.md
# 已知点的周围边权值。构造一个树图

import sys
sys.path.append("..")
from cflibs.cflibs import *
def main():
    n = II()
    p0 = []
    p1 = []

    for i in range(n):
        c, v = MII()
        if c: p1.append(v * n + i)
        else: p0.append(v * n + i)

    ans = []

    for _ in range(n - 1):
        v0, idx0 = divmod(p0.pop(), n)
        v1, idx1 = divmod(p1.pop(), n)
        
        if v0 <= v1 and p0:
            ans.append(f'{idx0 + 1} {idx1 + 1} {v0}')
            p1.append((v1 - v0) * n + idx1)
        else:
            ans.append(f'{idx0 + 1} {idx1 + 1} {v1}')
            p0.append((v0 - v1) * n + idx0)

    print('\n'.join(ans))