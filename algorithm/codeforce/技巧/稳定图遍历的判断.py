# https://codeforces.com/problemset/problem/2045/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0717/solution/cf2045g.md
# 图稳定的定义： 从A->B 随便选择路径，距离会有最小值
# 遍历是稳定的判定：  首先，图中所有环的权值和都只能为 0。否则，一个正环倒着走就成为了负环，于是可以中途绕路走这个负环任意多次，也就可以使得权值和任意小。
# 如果图是稳定的，A->B 距离就是 dist[A]  - dist[B]

import init_setting
from cflibs import *
def main():
    n, m, x = MII()
    grid = [[int(x) for x in I()] for _ in range(n)]
    
    d = {v: pow(v, x) for v in range(-9, 10)}
    
    dist = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if i: dist[i][j] = dist[i - 1][j] + d[grid[i - 1][j] - grid[i][j]]
            if j: dist[i][j] = dist[i][j - 1] + d[grid[i][j - 1] - grid[i][j]]
    
    flg = True
    for i in range(n):
        for j in range(m):
            if i and dist[i][j] != dist[i - 1][j] + d[grid[i - 1][j] - grid[i][j]]:
                flg = False
            if j and dist[i][j] != dist[i][j - 1] + d[grid[i][j - 1] - grid[i][j]]:
                flg = False
    
    q = II()
    outs = []
    
    for _ in range(q):
        x1, y1, x2, y2 = GMI()
        if flg: outs.append(str(dist[x2][y2] - dist[x1][y1]))
        else: outs.append('INVALID')
    
    print('\n'.join(outs))