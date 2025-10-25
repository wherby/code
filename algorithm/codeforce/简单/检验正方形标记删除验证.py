# https://codeforces.com/gym/106129/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1024/solution/cf106129f.md


import init_setting
from lib.cflibs import *
def main(): 
    n, m = MII()
    grid = [[1 if c == '#' else 0 for c in I()] for _ in range(n)]
    total = sum(sum(x) for x in grid)
    
    tmp = [[0] * m for _ in range(n)]
    
    for i in range(fmin(n, m), 0, -1):
        if total % (i * i) == 0:
            for x in range(n):
                for y in range(m):
                    tmp[x][y] = grid[x][y]
            
            flg = True
            for x in range(n):
                for y in range(m):
                    if tmp[x][y]:
                        for dx in range(x, x + i):
                            for dy in range(y, y + i):
                                if dx >= n or dy >= m or tmp[dx][dy] == 0:
                                    flg = False
                                    break
                                tmp[dx][dy] = 0
                            if not flg: break
                        if not flg: break
                if not flg: break
            
            if flg:
                print(i)
                break