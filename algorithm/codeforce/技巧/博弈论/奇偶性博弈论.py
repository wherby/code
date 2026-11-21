# https://codeforces.com/gym/106821/problem/H
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/11/1113/solution/cf106821h.md
# 这里奇偶性博弈论的时候，如果n的个数是偶数，且所有个数都>=2 则后手可以优先保持个数为偶数，镜像操作
import init_setting
from cflibs import *


def main():
    n = II()
    nums = LII()

    cnt = [0] * (n + 1)

    for x in nums:
        if x < n:
            cnt[x] += 1

    mex = 0

    while cnt[mex]:
        mex += 1

    if mex and (n % 2 or min(cnt[:mex]) == 1):
        print("Dinny")
    else:
        print("Tie")
