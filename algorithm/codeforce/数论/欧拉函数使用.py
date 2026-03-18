# https://codeforces.com/gym/106430/problem/H
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0318/solution/cf106430h.md
# 子问题： 对于x, 寻找 a+b=x 并且a,b互质的个数：  algorithm/mathA/gcd/数论GCD/phi函数的意义.md



import init_setting
from cflibs import *
def main(): 
    M = 2 * 10 ** 5
    
    phi = list(range(M + 1))
    
    phi[1] = 0
    for i in range(2, M + 1):
        if phi[i] == i:
            for j in range(i, M + 1, i):
                phi[j] = phi[j] // i * (i - 1)
    
    acc = [0] * (M + 1)
    
    for i in range(2, M + 1):
        if phi[i] == i - 1:
            for j in range(i, M + 1, i):
                acc[j] += phi[j // i]
    
    for i in range(1, M + 1):
        acc[i] += acc[i - 1]
    
    t = II()
    outs = []
    
    for _ in range(t):
        l, r = MII()
        outs.append(acc[r] - acc[l - 1])
    
    print('\n'.join(map(str, outs)))