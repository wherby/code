# https://codeforces.com/problemset/problem/1089/M
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0802/solution/cf1089m.md
# 已知各点的联通性，构造地图

import init_setting
from lib.cflibs import *
def main():
    n = II()
    grid = [LII() for _ in range(n)]
    
    ans = [[[-1] * (3 * n) for _ in range(3 * n)] for _ in range(3)]
    
    for i in range(n):
        idx = 3 * i + 1
        
        for j in range(3 * n):
            ans[0][idx][j] = 0
            ans[2][j][idx] = 0
        ans[2][-1][idx] = i + 1
    
        ans[1][idx-1][idx] = 0
        ans[1][idx-1][idx-1] = 0
        ans[0][idx-1][idx-1] = 0
        
        for j in range(n):
            if grid[i][j]:
                jdx = 3 * j + 1
                ans[0][idx-1][jdx] = 0
                ans[1][idx-1][jdx] = 0
                ans[2][idx-1][jdx] = 0
    
    print(3 * n, 3 * n, 3)
    for i in range(3):
        if i: print()
        print('\n'.join(''.join(str(x) if x > 0 else '#.'[x + 1] for x in y) for y in ans[i]))

main()