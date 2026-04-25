# https://codeforces.com/gym/105979/problem/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0413/solution/cf105979j.md
# algorithm/mathA/combination/docs/计数恒等式和组合恒等式.md
# 计数恒等式和 组合恒等式的使用


import init_setting
from cflibs import *
from lib.combineWithPreCompute import Factorial
def main(): 
    M = 10 ** 6 + 5
    mod = 998244353
    f = Factorial(M, mod)
    
    t = II()
    outs = []
    
    for _ in range(t):
        n, k = MII()
        outs.append(f.combi(n + 1, k + 1))
    
    print('\n'.join(map(str, outs)))