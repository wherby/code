# https://codeforces.com/gym/105562/problem/M
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0917/solution/cf105562m.md
# 多边型面积由三角形面积和计算，固定一点，取与此点不相连的边构成三角形面积就是多边面积
# 求多边形上端点可以构成的三角形的面积和？
#    这个时候，把三点编号，枚举中间点为 i,左右点的选择就是 [0,i), (i,n-1]
#.   由于高斯公式 是 abs((x2-x1)* (y3-y1) -(x3-x1)*(y2-y1))/2， 
#             因为点的方向是固定,所以，向量方向一致？ 所以可以把abs去掉？ 变成前后缀的向量计算
#               total_triangle_area += (i * x - pref_x) * (suff_y - (n - i - 1) * y) - (i * y - pref_y) * (suff_x - (n - i - 1) * x)
#       为什么向量可以去掉abs? 以任何一点为例，此点与0构成分割线，构成的三角形，分别在分割线两边，所以向量可以叠加
# algorithm/codeforce/几何图形/多边型图形面积和所有三角形面积和.py

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
    
    total_area = 0
    for i in range(2, n):
        dx1, dy1 = xs[i - 1] - xs[0], ys[i - 1] - ys[0]
        dx2, dy2 = xs[i] - xs[0], ys[i] - ys[0]
        total_area += dx1 * dy2 - dy1 * dx2
    
    total_triangle_area = 0
    
    pref_x = 0
    pref_y = 0
    
    suff_x = sum(xs)
    suff_y = sum(ys)
    
    for i in range(n):
        x = xs[i]
        y = ys[i]
        
        suff_x -= x
        suff_y -= y
        
        total_triangle_area += (i * x - pref_x) * (suff_y - (n - i - 1) * y) - (i * y - pref_y) * (suff_x - (n - i - 1) * x)
        
        pref_x += x
        pref_y += y
    
    print(total_triangle_area / total_area)