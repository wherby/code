# https://codeforces.com/gym/106123/problem/I
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/11/1113/solution/cf106123i.md
# algorithm/codeforce/几何图形/docs/对称性折叠和容斥.md

import init_setting
from lib.cflibs import *


def main():
    n, m = MII()

    ans = 0

    for i in range(1, n):
        for j in range(1, m):
            if math.gcd(i, j) == 1:
                l = fmin(n - i, i)
                r = fmin(m - j, j)
                ans += l * (m - j) + (n - i) * r - l * r

    print(ans)
