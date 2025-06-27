# https://codeforces.com/problemset/problem/132/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/06/0623/solution/cf132c.md
# 因为有左右两个方向，则把起始点放在n,用编码把2维空间压缩到1维。然后用第二维表示方向

import sys
sys.path.append("..")
from cflibs.cflibs import *
def main():
    s = I()
    k = II()

    n = len(s)

    dp = [[0] * (k + 1) * (2 * n + 1) for _ in range(2)]

    def f(i, j): return i * (2 * n + 1) + j

    dp[0][f(0, n)] = 1

    for c in s:
        ndp = [[0] * (k + 1) * (2 * n + 1) for _ in range(2)]
        
        if c == 'T':
            for i in range(2):
                for x in range(k + 1):
                    for y in range(2 * n + 1):
                        if dp[i][f(x, y)]:
                            ndp[i ^ 1][f(x, y)] = 1
                            if x < k:
                                ndp[i][f(x + 1, y + (-1 if i else 1))] = 1
        else:
            for i in range(2):
                for x in range(k + 1):
                    for y in range(2 * n + 1):
                        if dp[i][f(x, y)]:
                            ndp[i][f(x, y + (-1 if i else 1))] = 1
                            if x < k:
                                ndp[i ^ 1][f(x + 1, y)] = 1

        dp = ndp

    ans = 0

    for i in range(2):
        for x in range(k + 1):
            for y in range(2 * n + 1):
                if dp[i][f(x, y)] and (k - x) % 2 == 0:
                    ans = fmax(ans, abs(y - n))

    print(ans)