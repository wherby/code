# https://codeforces.com/gym/106796/problem/I
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/11/1118/solution/cf106796i.md
# 这里要枚举3,4 所有可能的节省操作，然后枚举3个4的选择量就可以倒推其他的节省操作了

import init_setting
from cflibs import *


def main():
    n = II()
    nums = LII()

    cnt = [0] * 5

    for x in nums:
        cnt[x % 5] += 1

    orig = cnt[1] + 2 * cnt[2]
    c4 = cnt[4]

    res = -n * 5

    for i in range(cnt[4] // 3 + 1):
        w3 = cnt[3]
        w4 = cnt[4] - i * 3
        cur = i * 2

        w = fmin(w3, w4)
        w3 -= w
        w4 -= w
        cur += w * 2

        w = w3 // 2
        cur += w
        w3 -= w * 2

        cur -= w3 * 2 + w4

        res = fmax(res, cur)

    print(res + orig)
