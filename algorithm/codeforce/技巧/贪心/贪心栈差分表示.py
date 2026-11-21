# https://codeforces.com/gym/106368/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/11/1119/solution/cf106368c.md
# to_use 从后到前贪心记录最大值，然后把淘汰值记录为0，然后利用差分还原时间

import init_setting
from cflibs import *


def main():
    n, D, t = MII()

    ds = []
    bs = []

    for _ in range(n):
        d, b = MII()
        ds.append(d)
        bs.append(b)

    to_use = [1] * n
    pq = []

    for i in range(n - 1, -1, -1):
        d = ds[i]
        b = bs[i]

        heappush(pq, bs[i] * n + i)

        while D - d + 1 < len(pq):
            to_use[heappop(pq) % n] = 0

    ans = 0
    for i in range(n):
        if to_use[i]:
            ans += bs[i]

    print(ans)

    if t == 2:
        for i in range(n - 1, 0, -1):
            to_use[i - 1] += to_use[i]

        for i in range(n):
            to_use[i] = fmin(D - to_use[i] + 1, D)

        print(" ".join(map(str, to_use)))
