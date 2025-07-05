# https://codeforces.com/problemset/problem/283/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/06/0628/solution/cf283d.md
# 分基数和偶数 有不同的dp逻辑， 用2分解之后，奇数偶数的情况统一

import sys
sys.path.append("..")
from cflibs.cflibs import *
def main():
    n = II()

    nums = LII()
    cnt2 = [0] * n

    for i in range(n):
        while nums[i] % 2 == 0:
            nums[i] //= 2
            cnt2[i] += 1

    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[j] % nums[i] == 0 and (cnt2[i] - cnt2[j] == i - j or cnt2[i] <= i - j - 1):
                dp[i] = fmax(dp[i], dp[j] + 1)

    print(n - max(dp))