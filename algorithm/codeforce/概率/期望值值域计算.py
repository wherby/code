
# https://codeforces.com/gym/105316/problem/H
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/12/1202/solution/cf105316h.md
# 如果计算每次的分布会比较困难
# algorithm/codeforce/概率/doc/期望化简.md
# 期望计算化简和  组合恒等式（Hockey-stick Identity / 曲棍球棒恒等式）


import init_setting
from cflibs import *
from lib.combineWithPreCompute import Factorial
def main(): 
    mod = 998244353
    M = 10 ** 5
    
    f = Factorial(M + 1, mod)
    
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        ans = 0
        
        for k in range(1, n + 1):
            ans += (n + 1) * f.inv(k + 1) % mod
            ans %= mod
        
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))
main()