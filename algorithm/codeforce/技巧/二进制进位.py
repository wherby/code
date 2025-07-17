# https://codeforces.com/problemset/problem/305/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0712/solution/cf305c.md
# 求 n个升序的二进制置位数的和的 表达

import init_setting
from cflibs import *
def main():
    n = II()
    nums = LII()

    cur = 0
    cnt = 0
    total = 0

    for v in nums:
        while cur < v and cnt:
            total += cnt % 2
            cur += 1
            cnt //= 2
        cur = v
        cnt += 1

    while cnt:
        total += cnt % 2
        cur += 1
        cnt //= 2

    print(cur - total)