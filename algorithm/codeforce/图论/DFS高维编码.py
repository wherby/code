# https://codeforces.com/gym/105580/problem/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/05/0528/solution/cf105580j.md
# 解法用 DFS高维编码的方式，把坐标和到达坐标的时候stack里的颜色用栈的值编码了
# if cur[-1] ^ i == 1: continue  利用相邻左右操作没有意义剪枝
# 这里每次进入该点的状态也是需要记录的，因为不同的步骤进入该点，后续的选择是不同的，所以构成了高维空间的DFS搜索
# if tuple(cur[-3:]) not in grid[nx][ny] and move(i):
#                grid[nx][ny].add(tuple(cur[-3:]))


import init_setting
from cflibs import *
def main():
    sys.setrecursionlimit(300000)
    
    n, m = MII()
    grid = [[set() for _ in range(2 * m + 1)] for _ in range(2 * n + 1)]
    
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    dir_str = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    
    cur = [-1, -1, -1]
    
    def move(idx):
        if idx < 4: print('MOVE', dir_str[idx], flush=True)
        else: print('BACK', flush=True)
        ret = I()
        if ret == 'EXIT': exit()
        if ret == 'FAIL': return False
        return True
    
    def f(x, y):
        for i in range(4):
            if cur[-1] ^ i == 1: continue
            
            cur.append(i)
            dx, dy = dirs[i]
            nx = x + dx
            ny = y + dy
            
            if tuple(cur[-3:]) not in grid[nx][ny] and move(i):
                grid[nx][ny].add(tuple(cur[-3:]))
                f(nx, ny)
                move(4)
            
            cur.pop()
    
    f(n, m)