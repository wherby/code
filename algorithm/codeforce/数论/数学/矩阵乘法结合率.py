# https://codeforces.com/gym/105022/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1006/solution/cf105022g.md
# 矩阵是由两个向量乘积得来，矩阵乘积的时候，用向量乘积为结合为标量减少矩阵运算

import init_setting
from cflibs import *

def main():
    n, k = MII()
    v1 = LII()
    v2 = LII()
    
    mod = 998244353
    tot1 = sum(v1) % mod
    tot2 = sum(v2) % mod
    dot_val = sum(v1[i] * v2[i] % mod for i in range(n)) % mod
    
    print(tot1 * tot2 % mod * pow(dot_val, k - 1, mod) % mod)