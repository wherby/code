# https://codeforces.com/gym/106826/problem/H
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/11/1116/solution/cf106826h.md
# 需要二分求数字大小，但是第二个mod 只有 0,1 这两个值，
# 所以需要先确定奇偶，然后使用二分查找， 查询的数字一定是奇数，因为需要知道余数是奇偶数推断是大于mid还是小于mid

import init_setting
from cflibs import *


def main():
    def query(x):
        print("?", x, flush=True)
        return II()

    def answer(x):
        print("!", x)

    start = 1 if query(2) == 1 else 2

    l = 0
    r = (10**9 - start) // 2

    while l < r:
        mid = (l + r) // 2

        w = start + 2 * mid + 1
        if w % 2 == 0:
            w += 1

        if query(w) == start % 2:
            r = mid
        else:
            l = mid + 1

    answer(start + 2 * l)
