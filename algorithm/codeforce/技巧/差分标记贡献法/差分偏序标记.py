# https://codeforces.com/gym/106728/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1001/solution/cf106728e.md
# 使用差分偏序标记哪些需要移动的路径，并且把不需要移动的格子记录路径经过的次数


import init_setting
from cflibs import *
def main():
    n = II()
    grid = [LGMI() for _ in range(n)]
    
    tag = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] // n == i:
                tag[i][j] |= 1
            if grid[i][j] % n == j:
                tag[i][j] |= 2
            
            if tag[i][j] == 0:
                exit(print('No'))
    
    block_tag = [[0] * n for _ in range(n)]
    
    for i in range(n):
        cur = -1
        diff = [0] * n
        
        for j in range(n):
            if tag[i][j] == 1:
                if grid[i][j] < cur:
                    exit(print('No'))
                cur = grid[i][j]
                
                l, r = grid[i][j] % n, j
                if l > r: l, r = r, l
                diff[l + 1] += 1
                diff[r] -= 1
        
        for j in range(1, n):
            diff[j] += diff[j - 1]
        
        for j in range(n):
            if diff[j] and tag[i][j] == 3:
                block_tag[i][j] += 1
    
    for j in range(n):
        cur = -1
        diff = [0] * n
        
        for i in range(n):
            if tag[i][j] == 2:
                if grid[i][j] < cur:
                    exit(print('No'))
                cur = grid[i][j]
                
                l, r = grid[i][j] // n, i
                if l > r: l, r = r, l
                diff[l + 1] += 1
                diff[r] -= 1
        
        for i in range(1, n):
            diff[i] += diff[i - 1]
        
        for i in range(n):
            if diff[i] and tag[i][j] == 3:
                block_tag[i][j] += 1
    
    for i in range(n):
        for j in range(n):
            if block_tag[i][j] == 2:
                exit(print('No'))
    
    print('Yes')