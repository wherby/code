# https://codeforces.com/gym/105453/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0312/solution/cf105453e.md
# 稠密图的Prim算法，记录每个点到已选点的最短距离，用一个虚拟节点连接所有节点。 所以初始的距离就是grid[i][i]，表示i点和虚拟节点之间的距离，每次选一个距离最短的点加入集合，并更新其他点到集合的距离。
# 


import init_setting
from cflibs import *
def main(): 
    n = II()
    grid = [LII() for _ in range(n)]
    
    ans = 0
    
    vis = [0] * n
    cur = [grid[i][i] for i in range(n)]
    
    for _ in range(n):
        chosen = -1
        
        for i in range(n):
            if not vis[i] and (chosen == -1 or cur[i] < cur[chosen]):
                chosen = i
        
        ans += cur[chosen]
        vis[chosen] = 1
        
        for j in range(n):
            cur[j] = fmin(cur[j], grid[chosen][j])
    
    print(ans)