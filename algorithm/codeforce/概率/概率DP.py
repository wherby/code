# https://codeforces.com/gym/104287/problem/K
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0106/solution/cf104287k.md
# 有两种方案数计算，？的分配对应的方案数， 分配完成之后，不同的字符串可以构成不同字符串的方案数
# 这个方案数的乘积就是替换？ 之后字符组合可以构成的独立字符串的方案数
# 分配的时候因为是和一定，可以用背包DP来计算这个过程

import init_setting
from cflibs import *
from lib.combineWithPreCompute import Factorial
def main(): 
    mod = 10 ** 9 + 7
    f = Factorial(1000, mod)
    
    t = II()
    outs = []
    
    rev26 = pow(26, -1, mod)
    pw_rev26 = [1] * 1001
    
    for i in range(1000):
        pw_rev26[i + 1] = pw_rev26[i] * rev26 % mod
    
    for _ in range(t):
        s = I()
        
        cnt = [0] * 26
        to_fill = 0
        
        for c in s:
            if 'a' <= c <= 'z':
                cnt[ord(c) - ord('a')] += 1
            else:
                to_fill += 1
        
        dp = [0] * (to_fill + 1)
        dp[0] = 1
        
        for i in range(26):
            for j in range(to_fill, -1, -1):
                if dp[j]:
                    for k in range(1, to_fill - j + 1):
                        dp[j + k] += dp[j] * f.fac_inv(cnt[i] + k) % mod * f.fac_inv(k) % mod
                        dp[j + k] %= mod
                    dp[j] = dp[j] * f.fac_inv(cnt[i]) % mod
        
        outs.append(dp[to_fill] * f.fac(to_fill) % mod * f.fac(len(s)) % mod * pw_rev26[to_fill] % mod)
    
    print('\n'.join(map(str, outs)))

main()