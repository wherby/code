# https://codeforces.com/gym/106356/problem/H
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/11/1112/solution/cf106356h.md
# 这里数字规模是 10**5,所以不可能枚举所有路径
# 这里 (𝑎𝑢⊕𝑎𝑣>𝑎𝑢)𝑎𝑛𝑑(𝑎𝑢⊕𝑎𝑣<𝑎𝑣) 的不等式，
# 则两个数字的最高位一定不相同，并且需要 小的数字的最高位 在大的数字的时候也是置位，这样的异或结果是在两数之间的
# 然后就用位数DP就可以得到答案

import init_setting
from cflibs import *


def main():
    t = II()
    outs = []

    for _ in range(t):
        n = II()
        nums = LII()

        path = [[0] * 61 for _ in range(61)]

        vis = [0] * 61
        dp = [1] * 61

        for x in nums:
            if x:
                k = x.bit_length() - 1
                vis[k] = 1

        for x in nums:
            k = x.bit_length() - 1
            for j in range(k):
                if x >> j & 1 and vis[j]:
                    path[j][k] = 1

        for i in range(61):
            for j in range(61):
                if path[i][j]:
                    dp[j] = fmax(dp[j], dp[i] + 1)

        outs.append(f"{max(dp)}")

    print("\n".join(outs))
