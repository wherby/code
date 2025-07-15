# https://codeforces.com/problemset/problem/45/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0714/solution/cf45j.md
# 构造不相邻的数字排列，用奇偶性分为黑白方块，大小数分别放不同颜色的方块


import sys
sys.path.append("..")
from cflibs.cflibs import *
def main():
    n, m = MII()

    if 2 < n + m < 5: print(-1)
    else:
        grid = [[0] * m for _ in range(n)]
        
        pt = 1
        for i in range(n):
            for j in range(m):
                if (i + j) % 2:
                    grid[i][j] = pt
                    pt += 1
        
        for i in range(n):
            for j in range(m):
                if (i + j) % 2 == 0:
                    grid[i][j] = pt
                    pt += 1
        
        print('\n'.join(' '.join(map(str, x)) for x in grid))