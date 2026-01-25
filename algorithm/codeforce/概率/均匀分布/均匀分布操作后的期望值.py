# https://codeforces.com/gym/105813/problem/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0120/solution/cf105813j.md
# 均匀分布的时候，每次操作之后的平均值不变？



import init_setting
from cflibs import *
from lib.combineWithPreCompute import *
def main(): 
    M = 2 * 10 ** 5
    mod = 10 ** 9 + 7
    f = Factorial(M, mod)
    
    t = II()
    outs = []
    
    for _ in range(t):
        n, k = MII()
        nums = LII()
        outs.append(sum(nums) % mod * f.inv(n) % mod)
    
    print('\n'.join(map(str, outs)))