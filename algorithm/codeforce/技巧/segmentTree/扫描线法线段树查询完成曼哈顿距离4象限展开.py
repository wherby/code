# https://codeforces.com/gym/106164/problem/L
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/05/0515/solution/cf106164l.md
# algorithm/mathA/abs/扫描线法线段树.md
# 扫描线的方式从上到下扫描，按照当前y值激活或者移除线段树中的点，然后使用x方向的坐标，完成在4个象限的线段树查询
# 使用y轴上排序的点控制扫描线，实现上下分割， 用查询点的x轴上的排序，控制线段树的查询范围实现左右分割。


import init_setting
from cflibs import *
from lib.segTreeWithFindFirst import *

def main():  
    n, q, a, b = MII()
    
    xs = []
    ys = []
    cs = []
    
    for _ in range(n):
        x, y, c = MII()
        xs.append(x)
        ys.append(y)
        cs.append(c)
    
    sorted_xs = sorted(xs)
    st_range_x = sorted(range(n), key=lambda x: xs[x])
    st_range_y = sorted(range(n), key=lambda x: ys[x])
    
    pos = [0] * n
    
    for i in range(n):
        pos[st_range_x[i]] = i
    
    qxs = []
    qys = []
    
    for _ in range(q):
        x, y = MII()
        qxs.append(x)
        qys.append(y)
    
    st_range_q = sorted(range(q), key=lambda x: qys[x])
    
    inf = 7 * 10 ** 18
    
    seg_up_left = SegTree(fmin, inf, arr=[-a * xs[i] + b * ys[i] + cs[i] for i in st_range_x])
    seg_up_right = SegTree(fmin, inf, arr=[a * xs[i] + b * ys[i] + cs[i] for i in st_range_x])
    seg_down_left = SegTree(fmin, inf, n)
    seg_down_right = SegTree(fmin, inf, n)
    
    outs = [0] * q
    pt = 0
    
    for i in st_range_q:
        while pt < n and ys[st_range_y[pt]] < qys[i]:
            idx = st_range_y[pt]
            seg_up_left.set(pos[idx], inf)
            seg_up_right.set(pos[idx], inf)
            seg_down_left.set(pos[idx], -a * xs[idx] - b * ys[idx] + cs[idx])
            seg_down_right.set(pos[idx], a * xs[idx] - b * ys[idx] + cs[idx])
            pt += 1
        
        p = bisect.bisect_left(sorted_xs, qxs[i])
        
        ans = inf
        ans = fmin(ans, seg_up_left.prod(0, p) + a * qxs[i] - b * qys[i])
        ans = fmin(ans, seg_up_right.prod(p, n) - a * qxs[i] - b * qys[i])
        ans = fmin(ans, seg_down_left.prod(0, p) + a * qxs[i] + b * qys[i])
        ans = fmin(ans, seg_down_right.prod(p, n) - a * qxs[i] + b * qys[i])
        
        outs[i] = ans
    
    print('\n'.join(map(str, outs)))

main()