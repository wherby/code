# https://codeforces.com/problemset/problem/209/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0725/solution/cf209a.md

import init_setting
from lib.cflibs import *
def main():
    n = II()
    mod = 10 ** 9 + 7
    
    dp0, dp1 = 0, 0
    
    for i in range(n):
        if i % 2 == 0:
            dp0 = (dp0 + dp1 + 1) % mod
        else:
            dp1 = (dp0 + dp1 + 1) % mod
    
    print((dp0 + dp1) % mod)