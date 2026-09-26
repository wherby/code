# https://codeforces.com/gym/106235/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0924/solution/cf106235a.md

import init_setting
from lib.cflibs import *
def main():
    n, k = MII()
    p = LII()
    s = LII()
    
    mod = 998244353
    f = Factorial(n, mod)
    
    ans = f.combi(n, k)
    
    for i in range(n):
        c = 0
        for j in range(n):
            if p[j] < p[i] and s[j] < s[i]:
                c += 1
        
        ans -= f.combi(c, k - 1)
        ans %= mod
    
    print(ans)