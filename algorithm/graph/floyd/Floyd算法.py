# https://codeforces.com/gym/106164/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/05/0512/solution/cf106164e.md
# 因为N,M 比较小，使用 FLOYD算法维护每条边加入的时候，从该点到其他店的最小距离
# 因为2号查询返回的是满足条件的最小节点，所以可以用前缀值预处理，使得用最后一个值来判定是否存在，然后查询最小符合条件的值


import init_setting
from cflibs import *
def main(): 
    n, m, q = MII()
    edges = []
    
    for _ in range(m):
        u, v, p, h = MII()
        u -= 1
        v -= 1
        edges.append((u, v, p, h))
    
    edges.sort(key=lambda x: x[2])
    
    inf = 10 ** 13
    
    dis = [[inf] * n for _ in range(n)]
    
    for i in range(n):
        dis[i][i] = 0
    
    saved = [[] for _ in range(n)]
    
    for i, (u, v, p, h) in enumerate(edges):
        for x in range(n):
            for y in range(n):
                dis[x][y] = fmin(dis[x][y], dis[x][u] + dis[v][y] + h)
        
        for x in range(n):
            saved[x].append(max(dis[x]))
    
    edges.reverse()
    
    for val in saved:
        val.reverse()
    
    min_saved = [val[:] for val in saved]
    
    for i in range(1, n):
        for j in range(m):
            min_saved[i][j] = fmin(min_saved[i][j], min_saved[i - 1][j])
    
    outs = []
    
    for _ in range(q):
        query = LII()
        
        if query[0] == 1:
            u = query[1] - 1
            h = query[2]
            
            l, r = 0, m - 1
            
            while l <= r:
                mid = (l + r) // 2
                
                if saved[u][mid] > h: r = mid - 1
                else: l = mid + 1
            
            if r < 0: outs.append('-1')
            else: outs.append(str(edges[r][2]))
        
        else:
            h = query[1]
            
            l, r = 0, m - 1
                
            while l <= r:
                mid = (l + r) // 2
                
                if min_saved[n - 1][mid] > h: r = mid - 1
                else: l = mid + 1
            
            if r < 0: outs.append('-1 -1')
            else:
                saved_r = r
                l = 0
                
                while l <= r:
                    mid = (l + r) // 2
                    
                    if edges[mid][2] == edges[saved_r][2]: r = mid - 1
                    else: l = mid + 1
                
                pos = l
                
                l, r = 0, n - 1
                
                while l <= r:
                    mid = (l + r) // 2
                    
                    if min_saved[mid][pos] <= h: r = mid - 1
                    else: l = mid + 1
                
                outs.append(f'{l + 1} {edges[pos][2]}')
    
    print('\n'.join(outs))