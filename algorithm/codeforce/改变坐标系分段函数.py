# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/03/0321/solution/cf590b.md
# https://codeforces.com/problemset/problem/590/B
from cflibs import *


def main():
    x1, y1, x2, y2 = MII()
    vm, t = MII()
    vx, vy = MII()
    wx, wy = MII()

    x2 -= x1
    y2 -= y1

    l, r = 0, 10 ** 9
    for _ in range(120):
        m = (l + r) / 2
        x, y = x2, y2
        x -= vx * fmin(m, t)
        y -= vy * fmin(m, t)
        x -= wx * (m - fmin(m, t))
        y -= wy * (m - fmin(m, t))
        
        if x * x + y * y <= vm * vm * m * m: r = m
        else: l = m

    print((l + r) / 2)