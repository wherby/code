# https://codeforces.com/gym/106632/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0803/solution/cf106632a.md
# 为什么不考虑 A = p1**m * p2**n 的形式，只考虑 质数的单一形式  A = p**m 
# 因为题目中求的是质数表示 数字，只需要知道每个质数在m内的最高次数就可以。其他形式一定能在最高次数下表示出来


import init_setting
from cflibs import *
def main():
    M = 10 ** 6 + 1
    isPrime = [1] * M
    cnt = [0] * M
    
    isPrime[0] = 0
    isPrime[1] = 0
    
    cnt[1] = 1
    
    for i in range(2, M):
        if isPrime[i]:
            for j in range(i * 2, M, i):
                isPrime[j] = 0
            
            v = i
            cur = 1
            
            while v < M:
                if cur & -cur == cur:
                    cnt[v] = 1
                v *= i
                cur += 1
    
    for i in range(1, M):
        cnt[i] += cnt[i - 1]
    
    t = II()
    outs = []
    
    for _ in range(t):
        outs.append(cnt[II()])
    
    print('\n'.join(map(str, outs)))