# https://codeforces.com/gym/105493/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0918/solution/cf105493c.md
# 利用相邻的差值在新坐标系上投影为正值来判定
# 向量排序算法
# cmp(i, j) ：向量按照辐角排序
# 利用首尾两个向量，合成新的坐标，使得首尾向量在新的坐标系投影为正
# 最后用最终的坐标系验证是否所有向量的投影都是正的
#  但是每个向量和其他向量的叉积会因为角度不同而得到不同的值，那怎么确定谁是最小值？
#    这是一个关于极角排序的常见误解。在极角排序中，我们并不需要计算每个向量的叉积并找到最小值。我们只需要用叉积来比较两个向量的相对位置。
#    排序算法（如快速排序或归并排序）的工作方式是：它需要一个比较函数来判断两个元素 A 和 B 谁应该排在前面。它不关心 A 和 B 具体的值，只关心 compare(A, B) 的结果是大于、小于还是等于零。


import init_setting
from lib.cflibs import *
def main():
    n = II()
    x, y = MII()
    
    if n == 1:
        print('YES')
        print(1, 0)
        print(0, 1)
        exit()
    
    xs = []
    ys = []
    
    for _ in range(n - 1):
        nx, ny = MII()
        xs.append(nx - x)
        ys.append(ny - y)
        x, y = nx, ny
    
    def cmp(i, j):
        xi, yi = xs[i], ys[i]
        xj, yj = xs[j], ys[j]
    
        v = xi * yj - yi * xj
        if v > 0: return 1
        if v < 0: return -1
        return 0
    
    st_range = sorted(range(n - 1), key=cmp_to_key(cmp))
    
    i1 = st_range[0]
    i2 = st_range[-1]
    
    x1, y1 = xs[i1], ys[i1]
    x2, y2 = xs[i2], ys[i2]
    
    if x1 * x2 + y1 * y2 >= 0:
        vx, vy = x1 + x2, y1 + y2
    else:
        vx1, vy1 = y1, -x1
        if vx1 * x2 + vy1 * y2 < 0: vx1, vy1 = -vx1, -vy1
        vx2, vy2 = y2, -x2
        if vx2 * x1 + vy2 * y1 < 0: vx2, vy2 = -vx2, -vy2
        vx, vy = vx1 + vx2, vy1 + vy2
    
    for i in range(n - 1):
        if vx * xs[i] + vy * ys[i] <= 0:
            exit(print('NO'))
    
    print('YES')
    print(vx, vy)
    print(-vy, vx)