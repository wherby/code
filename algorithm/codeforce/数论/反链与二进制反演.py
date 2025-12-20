# https://codeforces.com/gym/105775/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/12/1219/solution/cf105775d.md
# 题目求反链的最大长度， /Users/tao/software/code/algorithm/codeforce/数论/反链/Dilworth定理 则需要中间层的数目
# 而中间层的计算需要使用容斥原理 二进制反演计算 algorithm/codeforce/数论/二项式反演/index.md

import init_setting
from cflibs import *
from lib.combineWithPreCompute import *

def main(): 
    n, m = MII()
    mod = 998244353
    
    f = Factorial(n * m, mod)
    
    ans = 0
    target = n * (m + 1) // 2
    
    for i in range(target // (m + 1) + 1):
        total = target - i * m
        ans += f.comb(total - 1, n - 1) * f.comb(n, i) % mod * (1 if i % 2 == 0 else -1) % mod
        ans %= mod
    
    print(ans)
main()