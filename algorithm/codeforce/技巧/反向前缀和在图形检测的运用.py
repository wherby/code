# https://codeforces.com/problemset/problem/549/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0902/solution/cf549d.md
# 这个问题揭示了一个更有意思的问题，
#  实现二维数组的差分计算，在任意差分值不为0 的地方必然是特征值。
#  

import init_setting
from cflibs import *
def main():
    n, m = MII()
    grid = [[1 if c == 'B' else -1 for c in I()] for _ in range(n)]
    
    ans = 0
    
    for i in range(n):
        for j in range(m):
            v = grid[i][j]
            if i + 1 < n: v -= grid[i + 1][j]
            if j + 1 < m: v -= grid[i][j + 1]
            if i + 1 < n and j + 1 < m: v += grid[i + 1][j + 1]
            
            if v: ans += 1
    
    print(ans)