# https://codeforces.com/problemset/problem/1015/E1
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0731/solution/cf1015e1.md
# 设置任意星号为起点，并且用step来作为判定条件，只有step >1的时候才在tmp里标记


import init_setting
from lib.cflibs import *
def main():
    n, m = MII()
    
    grid = [[1 if c == '*' else 0 for c in I()] for _ in range(n)]
    tmp = [[0] * m for _ in range(n)]
    
    outs = []
    
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                ux, uy = i, j
                dx, dy = i, j
                lx, ly = i, j
                rx, ry = i, j
                
                step = 0
                while True:
                    ux -= 1
                    dx += 1
                    ly -= 1
                    ry += 1
                    
                    if ux >= 0 and dx < n and ly >= 0 and ry < m and grid[ux][uy] and grid[dx][dy] and grid[lx][ly] and grid[rx][ry]:
                        tmp[ux][uy] = 1
                        tmp[dx][dy] = 1
                        tmp[lx][ly] = 1
                        tmp[rx][ry] = 1
                        tmp[i][j] = 1
                        step += 1
                    else: break
                
                if step: outs.append(f'{i + 1} {j + 1} {step}')
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] != tmp[i][j]:
                exit(print(-1))
    
    print(len(outs))
    if outs: print('\n'.join(outs))