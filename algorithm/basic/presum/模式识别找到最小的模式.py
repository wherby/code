# https://codeforces.com/gym/105667/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0124/solution/cf105667b.md
# 模式识别，找打最小的模块
# 但是怎么在图形中标记模块？
# 在3个前缀和的图上标记了3个最小的模块识别值，标记了开始点
# 在判断的时候看区域是否这都在里面 《= 使用前缀和矩阵，因为是要区域都在中间，所以需要对坐标做相应偏移




import init_setting
from lib.cflibs import *

def main(): 
    n, m = MII()
    grid = [LII() for _ in range(n)]
    
    acc_13 = [[0] * (m + 1) for _ in range(n + 1)]
    acc_22 = [[0] * (m + 1) for _ in range(n + 1)]
    acc_31 = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(n):
        for j in range(m - 2):
            if grid[i][j] == grid[i][j + 1] and grid[i][j] == grid[i][j + 2]:
                acc_13[i + 1][j + 1] = 1
    
    for i in range(n - 1):
        for j in range(m - 1):
            if grid[i][j] == grid[i][j + 1] and grid[i][j] == grid[i + 1][j] and grid[i][j] == grid[i + 1][j + 1]:
                acc_22[i + 1][j + 1] = 1
    
    for i in range(n - 2):
        for j in range(m):
            if grid[i][j] == grid[i + 1][j] and grid[i][j] == grid[i + 2][j]:
                acc_31[i + 1][j + 1] = 1
    
    for i in range(n + 1):
        for j in range(m):
            acc_13[i][j + 1] += acc_13[i][j]
            acc_22[i][j + 1] += acc_22[i][j]
            acc_31[i][j + 1] += acc_31[i][j]
    
    for i in range(n):
        for j in range(m + 1):
            acc_13[i + 1][j] += acc_13[i][j]
            acc_22[i + 1][j] += acc_22[i][j]
            acc_31[i + 1][j] += acc_31[i][j]
    
    q = II()
    outs = []
    
    for _ in range(q):
        x1, y1, x2, y2 = MII()
        
        flg = True
        
        if y2 >= y1 + 2 and acc_13[x1][y1] - acc_13[x2 + 1][y1] - acc_13[x1][y2 - 1] + acc_13[x2 + 1][y2 - 1]:
            flg = False
        
        if x2 > x1 and y2 > y1 and acc_22[x1][y1] - acc_22[x2][y1] - acc_22[x1][y2] + acc_22[x2][y2]:
            flg = False
        
        if x2 >= x1 + 2 and acc_31[x1][y1] - acc_31[x2 - 1][y1] - acc_31[x1][y2 + 1] + acc_31[x2 - 1][y2 + 1]:
            flg = False
        
        outs.append('YES' if flg else 'NO')
    
    print('\n'.join(outs))