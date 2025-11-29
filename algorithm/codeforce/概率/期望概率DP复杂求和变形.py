# https://codeforces.com/gym/106208/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1124/solution/cf106208a.md
# DP 表达式拆项变形
# algorithm/codeforce/概率/doc/期望概率DP复杂求和变形.md

import init_setting
from cflibs import *
from lib.combineWithPreCompute import Factorial
def main(): 
    M = 2 * 10 ** 6
    mod = 998244353
    
    f = Factorial(M + 5, mod)
    
    dp = [0] * M
    dp[0] = 1
    
    v0 = 1
    v1 = 0
    
    for i in range(1, M):
        dp[i] = ((i + 1) * v0 - v1) % mod * 2 % mod * f.inv(i) % mod * f.inv(i + 3) % mod
        dp[i] = (dp[i] + 1) % mod
        v0 = (v0 + dp[i]) % mod
        v1 = (v1 + dp[i] * i) % mod
    
    t = II()
    rev2 = (mod + 1) // 2
    
    outs = []
    
    for _ in range(t):
        l, r = MII()
        outs.append((l + r) * rev2 % mod * dp[r - l] % mod)
    
    print('\n'.join(map(str, outs)))

main()