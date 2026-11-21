# https://codeforces.com/gym/106797/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/11/1107/solution/cf106797b.md
# “只能向上看”（单向辐射）
# 为什么根节点必须放烟花 algorithm/codeforce/图论/docs/贪心树上节点覆盖.md
#

import init_setting
from cflibs import *


def main():
    n, k = MII()
    parent = [-1] + LGMI()

    chosen = [0] * n
    dis = [0] * n

    for i in range(n - 1, 0, -1):
        if dis[i] == k - 1:
            chosen[i] = 1
        else:
            dis[parent[i]] = fmax(dis[parent[i]], dis[i] + 1)

    chosen[0] = 1

    print(sum(chosen))
    print(" ".join(f"{i + 1}" for i in range(n) if chosen[i]))
