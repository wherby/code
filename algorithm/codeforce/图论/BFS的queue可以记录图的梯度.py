# https://codeforces.com/gym/104670/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0725/solution/cf104670d.md
# 使用BFS先求最短路径
# 利用BFS顺序 遍历所有可能的移动，然后再求最终位置的可能值，这里其实没用到BFS梯度顺序的特点，BFS只是记录了所有可达的点



import init_setting
from cflibs import *
def main():
    m, n = MII()
    tmp = [I() for _ in range(n)]
    ops = I()
    
    grid = [[0] * m for _ in range(n)]
    sx, sy = -1, -1
    
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == '#': grid[i][j] = 1
            elif tmp[i][j] == 'S': sx, sy = i, j
    
    dis = [[-1] * m for _ in range(n)]
    
    def f(x, y): return x * m + y
    
    dis[sx][sy] = 0
    que = [f(sx, sy)]
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    for u in que:
        x, y = divmod(u, m)
        
        for dx, dy in dirs:
            if grid[x + dx][y + dy]: continue
            if dis[x + dx][y + dy] == -1:
                dis[x + dx][y + dy] = dis[x][y] + 1
                que.append(f(x + dx, y + dy))
    
    d = {
        'N': (-1, 0),
        'S': (1, 0),
        'W': (0, -1),
        'E': (0, 1)
    }
    
    l = len(ops)
    
    ans = [[0] * m for _ in range(n)]
    ans[sx][sy] = 1
    
    for u in que:
        x, y = divmod(u, m)
        
        if ans[x][y] and dis[x][y] < l:
            for c, (dx, dy) in d.items():
                if c != ops[dis[x][y]] and dis[x + dx][y + dy] == dis[x][y] + 1:
                    ans[x + dx][y + dy] = 1
    
    print('\n'.join(''.join(('!' if dis[i][j] == l and ans[i][j] else '.') if tmp[i][j] == '.' else tmp[i][j] for j in range(m)) for i in range(n)))