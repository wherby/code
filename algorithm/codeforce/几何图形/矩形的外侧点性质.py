# https://codeforces.com/gym/105442/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0615/solution/cf105442d.md
# 原题中保证了外围矩形与内侧矩形不相交，所以最外侧的点一定是个方向上当前的最大点，用标记的方式记录已经确定的点
# 可以想象四个方向的直线随着x,y轴慢慢与已知矩形点相切，如果是只用一个方向的话，有可能会同时碰到两个点，所以用了两个方向相切，这样保证每个最外侧的点只会遇到一个，用偏序打破了 两个点x或者y相等的情况


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
    
    o1 = sorted(range(n), key=lambda x: (xs[x], ys[x]))
    o2 = sorted(range(n), key=lambda x: (ys[x], -xs[x]))
    o3 = sorted(range(n), key=lambda x: (-xs[x], -ys[x]))
    o4 = sorted(range(n), key=lambda x: (-ys[x], xs[x]))
    
    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0
    
    vis = [0] * n
    
    for _ in range(n // 4 - 1):
        while vis[o1[p1]]: p1 += 1
        vis[o1[p1]] = 1
        
        while vis[o2[p2]]: p2 += 1
        vis[o2[p2]] = 1
        
        while vis[o3[p3]]: p3 += 1
        vis[o3[p3]] = 1
        
        while vis[o4[p4]]: p4 += 1
        vis[o4[p4]] = 1
    
    pts = []
    
    for i in range(n):
        if not vis[i]:
            pts.append((xs[i], ys[i]))
    
    x1, y1 = pts[0]
    x2, y2 = pts[1]
    x3, y3 = pts[2]
    
    dx1, dy1 = x2 - x1, y2 - y1
    dx2, dy2 = x3 - x1, y3 - y1
    
    print(abs(dx1 * dy2 - dy1 * dx2))
