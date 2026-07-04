# https://codeforces.com/gym/106607/problem/K
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0702/solution/cf106607k.md
# 使用CRT定理，得到独立循环节内，各个余数的方程组有且仅有唯一解的结论，使用乘法原理计算循环节内的合法位置 algorithm/codeforce/docs/数论/中国剩余定理CRT定义.md
# algorithm/codeforce/docs/数论/中国剩余定理CRT.md


import init_setting
from cflibs import *
def main():
    M = 10 ** 6 + 5
    isPrime = [1] * M
    
    primes = []
    for i in range(2, M):
        if isPrime[i]:
            primes.append(i)
            for j in range(i, M, i):
                isPrime[j] = 0
    
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        
        if n == 1:
            outs.append(1)
            continue
        
        pr = []
        
        cur = n
        for i in primes:
            if i * i > cur: break
            if cur % i == 0:
                pr.append(i)
            while cur % i == 0:
                cur //= i
        
        if cur > 1: pr.append(cur)
        
        total = 0
        if len(pr) == 1: total = (pr[0] - 1) * pr[0] // 2
        else:
            for i in range(1, pr[0]):
                res = 1
                for p in pr:
                    res *= p - i
                total += res
        
        ans = n
        for p in pr:
            ans //= p
        
        outs.append(ans * total % 998244353)
    
    print('\n'.join(map(str, outs)))