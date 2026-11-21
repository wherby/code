# https://codeforces.com/gym/106069/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/11/1121/solution/cf106069e.md

import init_setting
from lib.cflibs import *


def main():
    t = II()
    outs = []

    for _ in range(t):
        x, y, n = MII()

        total = x + 2 * y

        if total % n == 0:
            w = total // n

            if w % 2 * n <= x:
                outs.append("0")
                continue

        else:
            w, v = divmod(total, n)

            if w % 2 * (n - v) + (w + 1) % 2 * v <= x:
                outs.append("1")
                continue

        outs.append("2")

    print("\n".join(outs))


def min_imbalance(N, X, Y):
    k = Y % N
    S = X + 2 * Y
    if k + X < N:
        if k > 0:
            return 2
        return 0 if X == 0 else 1
    return 0 if S % N == 0 else 1
