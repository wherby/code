# https://codeforces.com/gym/106667/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0824/solution/cf106667f.md
# 这里其实是 N+2个特殊节点的最短路算法
# 由于上下两个特殊的节点的路径算法所以这里采用特殊处理
# 也可以用虚拟节点的算法求最短路径
# 这里是稠密图的dijstra 方法比使用Stack少了LoG（n)的复杂度

import init_setting
from cflibs import *
def main():
    n, h = MII()
    
    if n == 0: print(h)
    else:
        xs = []
        ys = []
        rs = []
    
        for _ in range(n):
            x, y, r = MII()
            xs.append(x)
            ys.append(y)
            rs.append(r)
    
        dis = [fmax(ys[i] - rs[i], 0) for i in range(n)]
        vis = [0] * n
    
        def f(i, j):
            return math.sqrt((xs[i] - xs[j]) * (xs[i] - xs[j]) + (ys[i] - ys[j]) * (ys[i] - ys[j]))
    
        for _ in range(n):
            chosen = -1
            for idx in range(n):
                if vis[idx] == 0 and (chosen == -1 or dis[idx] < dis[chosen]):
                    chosen = idx
            
            vis[chosen] = 1
            for i in range(n):
                dis[i] = fmin(dis[i], dis[chosen] + fmax(0, f(chosen, i) - rs[chosen] - rs[i]))
    
        ans = min(dis[i] + fmax(0, h - ys[i] - rs[i]) for i in range(n))
        print(f'{ans:.15f}')