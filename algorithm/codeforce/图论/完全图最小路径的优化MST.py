# https://codeforces.com/gym/106082/problem/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0925/solution/cf106082j.md
# 完全图最小路径遍历的优化
# 如果直接求所有路径然后放入堆栈 则有 N**2 *log(N**2)的复杂度
# 构造Minimum Spanning Tree (MST)  “Prim's Algorithm” 从0开始找到最近端点合并，
# 然后排序合并所有的点，标记最小路径



import init_setting
from cflibs import *
def main():
    n = II()
    xs = []
    ys = []
    
    for _ in range(n):
        x, y = MII()
        xs.append(x)
        ys.append(y)
    
    inf = 10 ** 15
    
    vis = [0] * n
    prev = [-1] * n
    mi_dis = [inf] * n
    
    vis[0] = 1
    mi_dis[0] = 0
    cur = 0
    
    edges = []
    
    for _ in range(n - 1):
        ncur = -1
        
        for i in range(n):
            if not vis[i]:
                nd = (xs[i] - xs[cur]) * (xs[i] - xs[cur]) + (ys[i] - ys[cur]) * (ys[i] - ys[cur])
                if nd < mi_dis[i]:
                    mi_dis[i] = nd
                    prev[i] = cur
                
                if ncur == -1 or mi_dis[i] < mi_dis[ncur]:
                    ncur = i
        
        cur = ncur
        vis[cur] = 1
        
        edges.append((mi_dis[cur] * n + prev[cur]) * n + cur)
    
    edges.sort()
    tmp = [[i] for i in range(n)]
    uf = list(range(n))
    
    ans = [[0] * n for _ in range(n)]
    
    for edge in edges:
        msk, v = divmod(edge, n)
        w, u = divmod(msk, n)
        
        u = uf[u]
        v = uf[v]
        
        for x in tmp[u]:
            for y in tmp[v]:
                ans[x][y] = w
                ans[y][x] = w
        
        for x in tmp[u]:
            tmp[v].append(x)
            uf[x] = v
        
        tmp[u].clear()
    
    outs = []
    q = II()
    
    for _ in range(q):
        u, v = GMI()
        outs.append(math.sqrt(ans[u][v]))
    
    print('\n'.join(map(str, outs)))