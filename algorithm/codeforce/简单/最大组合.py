# https://codeforces.com/gym/106603/problem/H
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/11/1104/solution/cf106603h.md
# e≈2.718281828459045… ？有关系吗？
# 所以优先选3，然后考虑余数

import init_setting
from lib.cflibs import *


def main():
    n = II()
    mod = 998244353

    n -= 2

    if n == 1:
        print(1)
    elif n % 3 == 0:
        print(pow(3, n // 3, mod))
    elif n % 3 == 2:
        print(2 * pow(3, n // 3, mod) % mod)
    else:
        print(4 * pow(3, n // 3 - 1, mod) % mod)
