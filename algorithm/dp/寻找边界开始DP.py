# https://codeforces.com/problemset/problem/38/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/05/0526/solution/cf38e.md
#TIPS# 寻找边界，从右到左滚动，则在最右开始的dp[0]=0，这样计算可以更好把一个大的问题变成已经解决的小问题，如果从左到右则不能使得问题规模变小

import sys
sys.path.append("..")
from cflibs.cflibs import *
def main():
    n = II()
    xs = []
    cs = []

    for _ in range(n):
        x, c = MII()
        xs.append(x)
        cs.append(c)

    order = sorted(range(n), key=lambda x: -xs[x])

    acc = [0] * (n + 1)
    for i in range(n):
        acc[i + 1] = acc[i] + xs[order[i]]

    inf = 10 ** 18
    dp = [inf] * (n + 1)

    dp[0] = 0

    for i in range(n):
        for j in range(i + 1):
            dp[i + 1] = fmin(dp[i + 1], dp[j] + cs[order[i]] + acc[i + 1] - acc[j] - xs[order[i]] * (i + 1 - j))

    print(dp[n])