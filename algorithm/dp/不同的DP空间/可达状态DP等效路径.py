# https://codeforces.com/gym/106825/problem/M
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/11/1118/solution/cf106825m.md
# 这里最优的是先排序再反转，所以三个起点开始搜索是最优的，
# 这里对每个位置值域进行DP得到三种路径的值，再在所有空间内计算状态数量
# 可达状态搜索
# 这里状态转移空间是对可达路径空间进行转换，而不是对最终值域DP

import init_setting
from cflibs import *


def main():
    n, k = MII()
    s = [int(c) for c in I()]
    s1 = sorted(s)
    s2 = sorted(s, reverse=True)

    mod = 998244353

    def f(x, y, z):
        return (x * (n + 1) + y) * (n + 1) + z

    M = (n + 1) * (n + 1) * (n + 1)
    dp = [0] * M
    ndp = [0] * M

    dp[0] = 1

    cnt = 0
    for i in range(n):
        step = i
        for x in range(step + 1):
            for y in range(step + 1):
                for z in range(step + 1):
                    if dp[f(x, y, z)]:
                        for d in range(2):
                            nx = x + (s[i] != d)
                            ny = y + (s1[i] != d)
                            nz = z + (s2[i] != d)
                            ndp[f(nx, ny, nz)] += dp[f(x, y, z)]

        step = i + 1
        for x in range(step + 1):
            for y in range(step + 1):
                for z in range(step + 1):
                    dp[f(x, y, z)] = ndp[f(x, y, z)] % mod
                    ndp[f(x, y, z)] = 0

    ans = 0
    for x in range(n + 1):
        for y in range(n + 1):
            for z in range(n + 1):
                if x <= k or y < k or z < k:
                    ans += dp[f(x, y, z)]

    print(ans % mod)
