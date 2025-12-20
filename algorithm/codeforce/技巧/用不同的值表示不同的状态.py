# https://codeforces.com/gym/105292/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/12/1219/solution/cf105292a.md
# 这里只需要每个空格都被照射，所以从上到下，从左到右遍历的时候，就可以了，不用考虑4个方向
# 如果每个点都循环判断则会超时，
# 在遍历的时候，用不同的值表示不同的状态，减少遍历次数



import init_setting
from cflibs import *
def main(): 
    n, m = MII()
    grid = [[0 if c == '.' else 1 for c in I()] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                grid[i][j] = 2
                
                for ni in range(i + 1, n):
                    if grid[ni][j] == 1: break
                    grid[ni][j] = 3
                
                for nj in range(j + 1, m):
                    if grid[i][nj] == 1: break
                    grid[i][nj] = 3
    
    print('\n'.join(''.join(" #L."[x] for x in y) for y in grid))