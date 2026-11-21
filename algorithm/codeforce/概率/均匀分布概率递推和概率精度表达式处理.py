# https://codeforces.com/gym/106806/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/11/1107/solution/cf106806a.md
#  algorithm/codeforce/概率/doc/均匀分布概率递推与高精度的数值计算.md
# 维护高精度数据的处理

import init_setting
from cflibs import *


def main():
    n = II()
    p = I()

    v1, v2 = p.split("e")
    v1 = float(v1)
    v2 = -int(v2)

    for _ in range(n):
        v1 *= 1.5 - 2 * (v1 * pow(0.1, v2)) ** 2
        while abs(v1) >= 10:
            v1 /= 10
            v2 -= 1

    print(f"{0.5 + v1 * pow(0.1, v2):.20f}")
