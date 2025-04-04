# https://codeforces.com/problemset/problem/766/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/04/0402/solution/cf766c.md
import sys
sys.path.append("..")
from cflibs.cflibs import *


def main():
    n = II()
    s = [ord(c) - ord('a') for c in I()]
    nums = LII()

    dp = [0] * (n + 1)
    dp[0] = 1

    mod = 10 ** 9 + 7

    for i in range(n):
        ma = n
        for j in range(i, n):
            ma = fmin(ma, nums[s[j]])
            if j - i + 1 > ma:
                break
            dp[j + 1] += dp[i]
            if dp[j + 1] >= mod:
                dp[j + 1] -= mod

    print(dp[n])

    dp = [0] * (n + 1)

    for i in range(n):
        ma = n
        for j in range(i, n):
            ma = fmin(ma, nums[s[j]])
            if j - i + 1 > ma:
                break
            dp[j + 1] = fmax(dp[j + 1], fmax(dp[i], j + 1 - i))

    print(dp[n])

    dp = [n] * (n + 1)
    dp[0] = 0

    for i in range(n):
        ma = n
        for j in range(i, n):
            ma = fmin(ma, nums[s[j]])
            if j - i + 1 > ma:
                break
            dp[j + 1] = fmin(dp[j + 1], dp[i] + 1)

    print(dp[n])