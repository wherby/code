# https://codeforces.com/problemset/problem/306/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/05/0523/solution/cf306c.md
# 先求出bad所有可能的组合数字，再求各类的全全排列数字
import sys
sys.path.append("..")
from cflibs.cflibs import *

def main():
    n, w, b = MII()
    mod = 10 ** 9 + 9

    f = Factorial(10000, mod)

    ans = 0

    for bad in range(1, n - 1):
        ans += f.combi(b - 1, bad - 1) * f.combi(w - 1, n - bad - 1) % mod * (n - 1 - bad) % mod
        ans %= mod

    print(ans * f.fac(w) % mod * f.fac(b) % mod)