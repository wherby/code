# https://codeforces.com/gym/106682/problem/N
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0904/solution/cf106682n.md
# 除了前面两位
# 长度为3的回文子串，其中回文子串的位置只与第3个位置的字母是否和第一个字母一样有关，但是不是回文的位置也只有a-1种可能
# 这里回文子串的选择其实是无后效性的组合

import init_setting
from cflibs import *
from lib.combineWithPreCompute import Factorial
def main():
    n, k, a = MII()
    mod = 998244353
    
    f = Factorial(n, mod)
    
    if n <= 2:
        if k > 0: print(0)
        else: print(pow(a, n, mod))
    else:
        print(a * a * f.combi(n - 2, k) % mod * pow(a - 1, n - 2 - k, mod) % mod)