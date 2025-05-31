# https://codeforces.com/problemset/problem/195/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/05/0527/solution/cf195d.md
# 直线斜率化简

import sys
sys.path.append("..")
from cflibs.cflibs import *
def main():
    n = II()
    vis = set()

    for _ in range(n):
        k, b = MII()
        g = math.gcd(k, b)
        if k:
            k //= g
            b //= g
            if k < 0 or (k == 0 and b < 0):
                k = -k
                b = -b
            vis.add((k, b))

    print(len(vis))