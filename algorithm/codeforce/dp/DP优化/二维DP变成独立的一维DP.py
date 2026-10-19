# https://codeforces.com/gym/104012/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1015/solution/cf104012e.md
# 题目看起来像是2维DP，其实两个方向相互独立，可以看成两个独立的一维DP


import init_setting
from cflibs import *
def main():
    n = II()
    grid = [I() for _ in range(n)]
    
    ans = 1
    mod = 998244353
    
    for i in range(n):
        dp0, dp1 = 1, 0
        
        for j in range(n):
            if grid[i][j] == '.':
                dp0, dp1 = (dp0 + dp1) % mod, 0
            elif grid[i][j] == '#':
                if j and grid[i][j - 1] == '#': continue
                dp0, dp1 = 0, dp0
            else:
                dp0, dp1 = dp0, (dp0 + dp1) % mod
        
        ans = ans * (dp0 + dp1) % mod
    
    for j in range(n):
        dp0, dp1 = 1, 0
        
        for i in range(n):
            if grid[i][j] == '.':
                dp0, dp1 = (dp0 + dp1) % mod, 0
            elif grid[i][j] == '#':
                if i and grid[i - 1][j] == '#': continue
                dp0, dp1 = 0, dp0
            else:
                dp0, dp1 = dp0, (dp0 + dp1) % mod
        
        ans = ans * (dp0 + dp1) % mod
    
    print(ans)