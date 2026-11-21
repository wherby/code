# https://codeforces.com/gym/106603/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/11/1103/solution/cf106603f.md
# 因为这里是保证输入的因子是随机的， 所以随机数能保证保持首项的单调递增的子序列理论是log(N)的规模，所以可以使用双层循环求解

import init_setting
from cflibs import *


def main():
    n = II()
    vals = [0] * (n + 1)

    for _ in range(n):
        s, v = MII()
        vals[s] = fmax(vals[s], v)

    dp = [0] * (n + 1)
    cur = 0

    for i in range(1, n + 1):
        if vals[i] > cur:
            cur = vals[i]
            for j in range(i, n + 1):
                dp[j] = fmax(dp[j], dp[j - i] + vals[i])

    print(" ".join(map(str, dp[1:])))
