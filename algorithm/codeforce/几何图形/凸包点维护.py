# https://codeforces.com/problemset/problem/406/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0806/solution/cf406d.md
# (y1 - y) /(x1 - x) < (y2 - y) /(x2 - x) 当前点与下一个点 比当前点与下下个点的斜率小，则构成凹包，则下一个点不是必经的点所以需要去掉
# stack里存了以当前点为凸包的店，每个店都是当前点做起始点必须经过的点，stack定点是必经的第一个点，stack的长度就是根到点的路径长度
# 然后用树上倍增的方法求LCA


import init_setting
from lib.cflibs import *
def main():
    n = II()
    xs = []
    ys = []
    
    for _ in range(n):
        x, y = MII()
        xs.append(x)
        ys.append(y)
    
    rs = list(range(n))
    stk = [n - 1]
    
    depth = [0] * n
    
    for i in range(n - 2, -1, -1):
        while len(stk) > 1:
            x, y = xs[i], ys[i]
            x1, y1 = xs[stk[-1]], ys[stk[-1]]
            x2, y2 = xs[stk[-2]], ys[stk[-2]]
            
            if (y1 - y) * (x2 - x) < (y2 - y) * (x1 - x):
                stk.pop()
            else:
                break
        
        rs[i] = stk[-1]
        depth[i] = depth[stk[-1]] + 1
        stk.append(i)
    
    nth_parent = [[0] * n for _ in range(20)]
    nth_parent[0] = rs
    
    for i in range(19):
        for j in range(n):
            nth_parent[i + 1][j] = nth_parent[i][nth_parent[i][j]]
    
    q = II()
    outs = []
    
    for _ in range(q):
        u, v = GMI()
        
        if depth[u] < depth[v]:
            u, v = v, u
        
        d = depth[u] - depth[v]
        
        while d:
            k = d & -d
            x = k.bit_length() - 1
            d -= k
            u = nth_parent[x][u]
        
        if u == v: outs.append(u + 1)
        else:
            for i in range(19, -1, -1):
                if nth_parent[i][u] != nth_parent[i][v]:
                    u = nth_parent[i][u]
                    v = nth_parent[i][v]
            
            outs.append(nth_parent[0][u] + 1)
    
    print(' '.join(map(str, outs)))