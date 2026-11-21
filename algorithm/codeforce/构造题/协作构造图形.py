# https://codeforces.com/gym/106788/problem/K
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/11/1102/solution/cf106788k.md
# 先用mask 选取最少方向能覆盖的组合
# 其实可以理解为规定了风车旋转方向，如果下一个选取，则保留给下一个位置

import init_setting
from lib.cflibs import *


def main():
    n = II()
    xs = []
    ys = []

    for _ in range(n):
        x, y = MII()
        xs.append(x)
        ys.append(y)

    tags = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    ans = 5
    chosen_msk = 0

    for i in range(16):
        flg = True

        for j in range(n):
            nflg = False

            for k in range(4):
                if i >> k & 1:
                    dx, dy = tags[k]
                    if xs[j] * dx + ys[j] * dy > 0:
                        nflg = True

            if not nflg:
                flg = False

        if flg and i.bit_count() < ans:
            ans = i.bit_count()
            chosen_msk = i

    chosen = [chosen_msk >> i & 1 for i in range(4)]

    ans = []

    if chosen[0]:
        if chosen[3]:
            ans.append("-0.4 0.6 1500.0 0.6 -0.4 1500.0 1500.0 1500.0")
        else:
            ans.append("-1500.0 0.6 1500.0 0.6 -1500.0 1500.0 1500.0 1500.0")

    if chosen[1]:
        if chosen[0]:
            ans.append("0.6 0.4 1500.0 0.4 0.6 -1500.0 1500.0 -1500.0")
        else:
            ans.append("0.6 1500.0 1500.0 1500.0 0.6 -1500.0 1500.0 -1500.0")

    if chosen[2]:
        if chosen[1]:
            ans.append("-1500.0 -0.6 0.4 -0.6 -1500.0 -1500.0 0.4 -1500.0")
        else:
            ans.append("-1500.0 -0.6 1500.0 -0.6 -1500.0 -1500.0 1500.0 -1500.0")

    if chosen[3]:
        if chosen[2]:
            ans.append("-1500.0 -0.4 -0.6 -0.4 -1500.0 1500.0 -0.6 1500.0")
        else:
            ans.append("-1500.0 -1500.0 -0.6 -1500.0 -1500.0 1500.0 -0.6 1500.0")

    print(len(ans))
    print("\n".join(ans))
