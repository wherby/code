# https://codeforces.com/gym/104879/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0704/solution/cf104879c.md
# 原题中 A[i][j] = a+b ,A[i+a][j]=b ,A[i][j+b] = a 
# 转换计算  A[i][j] - A[i+a][j] = a , A[i][j] - A[i][j+b] = b 
# 这样就有统一的参数系数


import init_setting
from cflibs import *
def main():
    n, m = MII()
    grid = [LII() for _ in range(n)]
    
    rnd = random.getrandbits(30)
    
    cnt = [[0] * m for _ in range(n)]
    
    for i in range(n):
        d = Counter()
        for j in range(m - 1, -1, -1):
            cnt[i][j] = d[grid[i][j] + j + rnd]
            d[grid[i][j] + j + rnd] += 1
    
    ans = 0
    for j in range(m):
        d = Counter()
        for i in range(n - 1, -1, -1):
            ans += cnt[i][j] * d[grid[i][j] + i + rnd]
            d[grid[i][j] + i + rnd] += 1
    
    print(ans)