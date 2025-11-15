# https://codeforces.com/gym/105962/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1112/solution/cf105962c.md
# 遍历所有可能的行组合，在上下都是1 的情况组合列的值

import init_setting
from lib.cflibs import *
def main(): 
    n = II()
    grid = [[int(c) for c in I()] for _ in range(n)]
    
    ans = 0
    
    cnt = [0] * n
    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                cnt[j] += 1
                ans = 1
    
    for i in range(n):
        for j in range(i):
            v = 0
            w = 0
            for k in range(n):
                if grid[i][k] and grid[j][k]:
                    v += 1
                    w = fmax(w, cnt[k])
    
            ans = fmax(ans, fmin(v, w))
    
    print(ans)