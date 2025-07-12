# https://codeforces.com/problemset/problem/183/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0710/solution/cf183b.md
# 直线方程是 y-y1 = (dy/dx) *(x-x1)   
# 展开  dy*x - dx * y + (dx*y1 - dy*x1) =0
# 如果要求到 x轴带上的截距，设 y =0 ;则 x = (dy*x1-dx*y1) /dy
# 因为是每个整数点上可以看到的最多鸟的数量，所以截距是整数的时候，选择最多的那条
# int(sqrt( (1+2+...+i) *2 )) == i 

import sys
sys.path.append("..")
from cflibs.cflibs import *

def main():
    n, m = MII()
    xs = []
    ys = []

    for _ in range(m):
        x, y = MII()
        xs.append(x)
        ys.append(y)

    cnt = Counter()

    for i in range(m):
        x1, y1 = xs[i], ys[i]
        for j in range(i):
            x2, y2 = xs[j], ys[j]
            dx, dy = x2 - x1, y2 - y1
            
            g = math.gcd(dx, dy)
            dx //= g
            dy //= g
            
            if dx < 0 or (dx == 0 and dy < 0):
                dx = -dx
                dy = -dy
            
            cnt[(dx, dy, x1 * dy - dx * y1)] += 1

    ans = [0] * (n + 1)

    for dx, dy, val in cnt:
        v = cnt[(dx, dy, val)]
        if dy and val % dy == 0 and 1 <= val // dy <= n:
            ans[val // dy] = fmax(ans[val // dy], v)

    res = 0
    for i in range(1, n + 1):
        res += math.isqrt(ans[i] * 2) + 1

    print(res)