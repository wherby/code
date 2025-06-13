# https://codeforces.com/problemset/problem/303/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/06/0611/solution/cf303b.md
# 求矩形中最大的固定矩形的最小坐标位置
# 其中对于x0,y0的讨论

import sys
sys.path.append("..")
from cflibs.cflibs import *
def main():
    n, m, x, y, a, b = MII()
    g = math.gcd(a, b)
    a //= g
    b //= g

    t = fmin(n // a, m // b)
    v, w = t * a, t * b

    x0 = fmin(n - v, fmax(x - (v + 1) // 2, 0))
    y0 = fmin(m - w, fmax(y - (w + 1) // 2, 0))

    print(x0, y0, x0 + v, y0 + w)