# https://codeforces.com/problemset/problem/605/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/04/0412/solution/cf605a.md

from cflibs import *
def main():
    n = II()
    nums = LII()

    dp = [0] * (n + 1)
    for v in nums:
        dp[v] = dp[v - 1] + 1

    print(n - max(dp))