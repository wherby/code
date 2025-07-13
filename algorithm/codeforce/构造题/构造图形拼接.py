# https://codeforces.com/problemset/problem/86/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0711/solution/cf86b.md
# 原题是需要2-5个联通区域覆盖空格
# 所以构造的时候，先构造2个联通区域， 如果向右和向下不能构造出联通区域，则向上，向左找到联通区域进行合并，如果找不到，则不满足条件
#

import sys
sys.path.append("..")
from cflibs.cflibs import *
def main():
    n, m = MII()
    grid = [[-1 if c == '#' else -2 for c in I()] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if grid[i][j] == -2:
                c = (i % 3) + (j % 3) * 3
                grid[i][j] = c
                if j + 1 < m and grid[i][j + 1] == -2:
                    grid[i][j + 1] = c
                elif i + 1 < n and grid[i + 1][j] == -2:
                    grid[i + 1][j] = c
                else:
                    if j and grid[i][j - 1] != -1: grid[i][j] = grid[i][j - 1]
                    elif i and grid[i - 1][j] != -1: grid[i][j] = grid[i - 1][j]
                    elif j + 1 < m and grid[i][j + 1] != -1: grid[i][j] = grid[i][j + 1]
                    else: exit(print(-1))

    print('\n'.join(''.join('#' if x == -1 else str(x) for x in y) for y in grid))