# https://codeforces.com/gym/106049/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/12/1230/solution/cf106049e.md
# 为了维护新值，作用 dp值来记录最新的值的大小，比遍历逻辑简单，多了N次读取
# 跟新的时候第二次不需要重新寻路

import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n, q = MII()
        grid = [LII() for _ in range(n)]
        
        saved = [0] * (2 * n - 1)
        dp = [[0] * n for _ in range(n)]
        
        for _ in range(q):
            k, v = MII()
            k -= 2
            
            if saved[k]:
                dp[n - 1][n - 1] += v - saved[k]
                saved[k] = v
            else:
                saved[k] = v
                for i in range(n):
                    for j in range(n):
                        if saved[i + j] > 0:
                            grid[i][j] = saved[i + j]
                        dp[i][j] = grid[i][j]
                
                for i in range(n):
                    for j in range(n):
                        w = 0
                        if i: w = fmax(w, dp[i - 1][j])
                        if j: w = fmax(w, dp[i][j - 1])
                        dp[i][j] += w
            
            outs.append(dp[n - 1][n - 1])
    
    print('\n'.join(map(str, outs)))