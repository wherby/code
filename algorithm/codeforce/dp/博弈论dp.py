# https://codeforces.com/problemset/problem/39/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/06/0604/solution/cf39e.md
# 求各个边界情况，然后往中心推演。 由于平局是独立的情况，所以在从边界往中心推导的时候，只要不是平局就可以反转。

import sys
sys.path.append("..")
from cflibs.cflibs import *
def main():
    a, b, n = MII()

    dp = [[-1] * (10 ** 5) for _ in range(32)]

    for i in range(1, 32):
        for j in range(1, 10 ** 5):
            if dp[i][j - 1] == 0 or j ** i >= n: dp[i][j] = 0

    if dp[1][-1] == -1: dp[1][-1] = (n - a) & 1

    for i in range(1, 32):
        if dp[i - 1][1] == 2 or 1 << i >= n:
            dp[i][1] = 2

    for i in range(30, 0, -1):
        for j in range(10 ** 5 - 2, 0, -1):
            if dp[i][j] == -1:
                if dp[i + 1][j] == 1 or dp[i][j + 1] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1

    ans = ["Masha", "Stas", "Missing"]

    print(ans[dp[b][a]])