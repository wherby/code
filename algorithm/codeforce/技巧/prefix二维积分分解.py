# https://codeforces.com/problemset/problem/2044/H
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/06/0618/solution/cf2044h.md
# 原题中和式包含了在区域中 A(ij)*Idx(ij)， 可以通过xy分解为和x,y相关的前缀和
# 求区域中所以点的和式，需要定义（x,y)求和式，再合并到区域里

import sys
sys.path.append("..")
from cflibs.cflibs import *
def main():
    t = II()
    outs = []

    for _ in range(t):
        n, q = MII()
        grid = [LII() for _ in range(n)]
        
        pref_orig = [[0] * (n + 1) for _ in range(n + 1)]
        pref_x = [[0] * (n + 1) for _ in range(n + 1)]
        pref_y = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(n):
            for j in range(n):
                pref_orig[i + 1][j + 1] = grid[i][j]
                pref_x[i + 1][j + 1] = grid[i][j] * i
                pref_y[i + 1][j + 1] = grid[i][j] * j
        
        for i in range(n + 1):
            for j in range(n):
                pref_orig[i][j + 1] += pref_orig[i][j]
                pref_x[i][j + 1] += pref_x[i][j]
                pref_y[i][j + 1] += pref_y[i][j]
        
        for i in range(n):
            for j in range(n + 1):
                pref_orig[i + 1][j] += pref_orig[i][j]
                pref_x[i + 1][j] += pref_x[i][j]
                pref_y[i + 1][j] += pref_y[i][j]
        
        ans = []
        for _ in range(q):
            x1, y1, x2, y2 = MII()
            orig = pref_orig[x2][y2] - pref_orig[x1 - 1][y2] - pref_orig[x2][y1 - 1] + pref_orig[x1 - 1][y1 - 1]
            vx = pref_x[x2][y2] - pref_x[x1 - 1][y2] - pref_x[x2][y1 - 1] + pref_x[x1 - 1][y1 - 1]
            vy = pref_y[x2][y2] - pref_y[x1 - 1][y2] - pref_y[x2][y1 - 1] + pref_y[x1 - 1][y1 - 1]
            ans.append(vx * (y2 - y1 + 1) + vy + (1 - (y1 - 1) - (x1 - 1) * (y2 - y1 + 1)) * orig)
        
        outs.append(' '.join(map(str, ans)))

    print('\n'.join(outs))