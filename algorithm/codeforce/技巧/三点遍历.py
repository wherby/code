# https://codeforces.com/problemset/problem/1453/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/06/0612/solution/cf1453c.md
# 要求三个点的最大值，其中一个点可以任意选，如果求另一条边的最大值，不是遍历两点，而是用当前点和最大最小边界构成

import sys
sys.path.append("..")
from cflibs.cflibs import *
def main():
    t = II()
    outs = []

    for _ in range(t):
        n = II()
        grid = [[int(x) for x in I()] for _ in range(n)]
        
        min_x = [n + 1] * 10
        min_y = [n + 1] * 10
        max_x = [-1] * 10
        max_y = [-1] * 10
        
        for i in range(n):
            for j in range(n):
                min_x[grid[i][j]] = fmin(min_x[grid[i][j]], i)
                min_y[grid[i][j]] = fmin(min_y[grid[i][j]], j)
                max_x[grid[i][j]] = fmax(max_x[grid[i][j]], i)
                max_y[grid[i][j]] = fmax(max_y[grid[i][j]], j)
        
        ans = [0] * 10
        
        for i in range(n):
            for j in range(n):
                ans[grid[i][j]] = fmax(ans[grid[i][j]], fmax(i, n - 1 - i) * fmax(max_y[grid[i][j]] - j, j - min_y[grid[i][j]]))
                ans[grid[i][j]] = fmax(ans[grid[i][j]], fmax(j, n - 1 - j) * fmax(max_x[grid[i][j]] - i, i - min_x[grid[i][j]]))
        
        outs.append(ans)

    print('\n'.join(' '.join(map(str, out)) for out in outs))