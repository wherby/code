# https://codeforces.com/gym/102556/problem/I
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0325/solution/cf102556i.md
# 三角形内的点的统计，如果暴力计算的话需要 N**4 的复杂度，这里采用了向量分解《= 有向贡献分解 algorithm/codeforce/几何图形/docs/三角形内部点的计数.md
# 步骤如下： algorithm/codeforce/几何图形/docs/三角形几何计算分析.md
# (x2 - x1) * (y - y1) > (x - x1) * (y2 - y1) 用来标记 点(x,y)在 （x1,y1)->(x2,y2) 向量的左边还是右边
# 这时选第一个点作为坐标极点，可以和其他任意一个线段构成三角形，
# 预处理 i,j坐标点和坐标极点 构成的三角形内有多少个点
# 然后利用 cnt = abs(area(i, j) + area(j, k) - area(i, k)) 计算3条边和极点构成的三个三角形 就是三角形内部的和
# 然后因为0 点如果在三角形内，则没有被计入，则需要计入 +1
# 如果0在三角形外，则有可能其中一个顶点在0 与另外两个点构成的三角形内，如果这样的话，就要 -1

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
    
    pre = [[0] * n for _ in range(n)]
    
    def is_in(to_check, i, j, k):
        x, y = xs[to_check], ys[to_check]
        x1, y1 = xs[i], ys[i]
        x2, y2 = xs[j], ys[j]
        x3, y3 = xs[k], ys[k]
        
        return (x2 - x1) * (y - y1) > (x - x1) * (y2 - y1) and\
            (x3 - x2) * (y - y2) > (x - x2) * (y3 - y2) and\
            (x1 - x3) * (y - y3) > (x - x3) * (y1 - y3)
    
    for i in range(1, n):
        for j in range(i + 1, n):
            for k in range(1, n):
                if k != i and k != j and (is_in(k, 0, i, j) or is_in(k, 0, j, i)):
                    pre[i][j] += 1
    
    def area(x, y):
        x1, y1 = xs[x] - xs[0], ys[x] - ys[0]
        x2, y2 = xs[y] - xs[0], ys[y] - ys[0]
        return pre[x][y] if x1 * y2 > x2 * y1 else -pre[x][y]
    
    ans = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                cnt = abs(area(i, j) + area(j, k) - area(i, k))
                if is_in(0, i, j, k) or is_in(0, i, k, j):
                    cnt += 1
                elif is_in(i, 0, j, k) or is_in(i, 0, k, j):
                    cnt -= 1
                elif is_in(j, 0, i, k) or is_in(j, 0, k, i):
                    cnt -= 1
                elif is_in(k, 0, i, j) or is_in(k, 0, j, i):
                    cnt -= 1
                ans += math.comb(cnt, 3)
    
    print(ans)



