# https://codeforces.com/problemset/problem/285/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0714/solution/cf285d.md

import sys
sys.path.append("..")
from cflibs.cflibs import *
def main():
    ans = [0, 1, 0, 3, 0, 15, 0, 133, 0, 2025, 0, 37851, 0, 1030367, 0, 36362925, 0]

    n = II()
    mod = 10 ** 9 + 7
    print(ans[n] * math.factorial(n) % mod)