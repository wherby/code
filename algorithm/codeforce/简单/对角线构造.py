# https://codeforces.com/gym/104887/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0810/solution/cf104887c.md
# 对角线构造k次操作


import init_setting
from lib.cflibs import *

def main():
    t = II()
    outs = []
    
    for _ in range(t):
        r, c, m, k = MII()
        
        if k > fmin(r, c): outs.append('NO')
        elif m < k or m > fmax(r, c) * k: outs.append('NO')
        else:
            grid = [[0] * c for _ in range(r)]
            
            for i in range(k):
                grid[i][i] = 1
                m -= 1
    
            for i in range(k if r < c else r):
                for j in range(k if c < r else c):
                    if m and grid[i][j] == 0:
                        grid[i][j] = 1
                        m -= 1
            
            outs.append('YES')
            outs.append('\n'.join(''.join('.#'[v] for v in x) for x in grid))
    
    print('\n'.join(outs))