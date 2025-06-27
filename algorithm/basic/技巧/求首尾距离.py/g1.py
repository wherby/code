# https://codeforces.com/problemset/problem/58/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/06/0624/solution/cf58c.md
# 求首尾距离只需要遍历一次就可以得到对称位置的距离

import sys
sys.path.append("..")
from cflibs.cflibs import *

def main():
    n = II()
    nums = LII()

    cnt = [0] * (10 ** 5 + 1)

    for i in range(n):
        x = nums[i] - fmin(i, n - 1 - i)
        if x > 0:
            cnt[x] += 1

    print(n - max(cnt))