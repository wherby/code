# https://codeforces.com/problemset/problem/275/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/05/0521/solution/cf275b.md
# 判定同行/列 是否分离
# 判定不同行列的转折点是否为黑色

import init_setting
from lib.cflibs import *
def main():
    n, m = MII()
    grid = [[1 if c == 'B' else 0 for c in I()] for _ in range(n)]

    for i in range(n):
        cur = 0
        blocks = 1
        
        for j in range(m):
            if grid[i][j] != cur:
                cur = grid[i][j]
                blocks += 1
        
        if blocks >= 4: exit(print('NO'))

    for j in range(m):
        cur = 0
        blocks = 1
        
        for i in range(n):
            if grid[i][j] != cur:
                cur = grid[i][j]
                blocks += 1
        
        if blocks >= 4: exit(print('NO'))

    for i1 in range(n):
        for j1 in range(m):
            for i2 in range(n):
                for j2 in range(m):
                    if grid[i1][j1] and grid[i2][j2] and not grid[i1][j2] and not grid[i2][j1]:
                        exit(print('NO'))

    print('YES')