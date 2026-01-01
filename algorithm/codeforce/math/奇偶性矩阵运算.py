# https://codeforces.com/gym/106039/problem/L
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/12/1209/solution/cf106039l.md
# nextState = CurState ^ Neighbors, nextState 是由 包括自己的 9 个状态决定的，在矩阵运算中计算这些状态
# 因为奇数个数反转，偶数个不变，则符合奇偶性

import init_setting
from cflibs import *
from lib.max_pow_mod2 import *
def main(): 
    n, k = MII()
    grid = [I() for _ in range(n)]
    
    def f(i, j): return i * n + j
    
    transition = [[0] * (n * n) for _ in range(n * n)]
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] != '#':
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        ni = i + di
                        nj = j + dj
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] != '#':
                            transition[f(i, j)][f(ni, nj)] = 1
    
    kth_transition = matrix_pow(transition, k)
    
    ans = [[0] * n for _ in range(n)]
    for x1 in range(n):
        for y1 in range(n):
            for x2 in range(n):
                for y2 in range(n):
                    if kth_transition[f(x1, y1)][f(x2, y2)] and grid[x1][y1] == '1':
                        ans[x2][y2] ^= 1
    
    print('\n'.join(''.join(str(ans[i][j]) if grid[i][j] != '#' else '#' for j in range(n)) for i in range(n)))

main()