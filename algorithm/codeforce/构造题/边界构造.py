# https://codeforces.com/problemset/problem/815/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/06/0605/solution/cf815a.md
# 从边界开始构造， 如果符合条件之后（因为匹配了所有点），只用一行和一列就能完全求出值
# 不符合的条件判定
import sys
sys.path.append("..")
from cflibs.cflibs import *

def main():
    n, m = MII()
    grid = [LII() for _ in range(n)]

    flg = True
    for i in range(n):
        for j in range(m):
            if grid[0][0] + grid[i][j] != grid[i][0] + grid[0][j]:
                flg = False

    if not flg:
        print(-1)
    else:
        v = min(grid[0]) if n < m else grid[0][0] - min(grid[i][0] for i in range(n))
        outs = []
        
        for _ in range(v):
            outs.append(f'row 1')
        
        for _ in range(grid[0][0] - v):
            outs.append(f'col 1')
        
        for i in range(1, n):
            for _ in range(grid[i][0] - (grid[0][0] - v)):
                outs.append(f'row {i + 1}')
        
        for i in range(1, m):
            for _ in range(grid[0][i] - v):
                outs.append(f'col {i + 1}')
        
        print(len(outs))
        print('\n'.join(outs))