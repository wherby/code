# https://codeforces.com/gym/104882/problem/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0810/solution/cf104882j.md
# 这里的生成区域的时候，如果刚好生成 k%m == m-1 个区域的时候，最后用的挡板就会形成新的区域，所以需要微调减少一个区域 
# 减少区域的情况只有下面还有一排的时候才能成立

# k=9
#  (行0)  0  1  0  1  0
#  (行1)  1  0  1  0  1
#  (行2)  1  0  1  0  1   <-- 复制第 1 行
#  (行3)  1  0  1  0  1   <-- 复制第 1 行
# 特殊处理之后
#  (行0)  0  1  0  1  0
#  (行1)  1  0  1  0  0
#  (行2)  1  0  1  0  1   <-- 复制第 1 行
#  (行3)  1  0  1  0  1   <-- 复制第 1 行


# k=8 n=4,m=5
#  (行0)  0  1  0  1  0
#  (行1)  1  0  1  0  0
#  (行2)  1  0  1  0  0
#  (行3)  1  0  1  0  0

import init_setting
from lib.cflibs import *
def main():
    n, m, k = MII()
    
    if n == 1:
        print('YES')
        print(''.join(str(fmin(i, k - 1) % 2) for i in range(m)))
    elif m == 1:
        print('YES')
        print('\n'.join(str(fmin(i, k - 1) % 2) for i in range(n)))
    elif k == n * m - 1:
        print('NO')
    else:
        grid = [[-1] * m for _ in range(n)]
        
        if k <= m:
            for i in range(n):
                for j in range(m):
                    grid[i][j] = fmin(j, k - 1) % 2
        else:
            first = (k - 1) // m + 1
            for i in range(first):
                for j in range(m):
                    if i * m + j <= k:
                        grid[i][j] = (i + j) % 2
                    else:
                        grid[i][j] = 1 - (i + j) % 2
            
            for i in range(first, n):
                for j in range(m):
                    grid[i][j] = grid[i - 1][j]
            
            if k % m == m - 1:
                grid[first - 1][m - 1] = grid[first - 2][m - 1]
        
        print('YES')
        print('\n'.join(''.join(map(str, x)) for x in grid))