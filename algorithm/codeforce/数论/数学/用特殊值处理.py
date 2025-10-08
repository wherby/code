# https://codeforces.com/gym/104679/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1008/solution/cf104679e.md
# 求已知图形里的分离区域，已经连接的区域是质数和它的合数
# 这里用2这个特殊的值， 因为任何一个质数的第一个合数就是2倍，如果在N范围内质数有2倍，则被连接，否则就是独立的区域
# 然后用前缀和解决


import init_setting
from cflibs import *
def main():
    M = 10 ** 7
    is_prime = [1] * (M + 1)
    is_prime[0] = 0
    is_prime[1] = 0
    
    for i in range(2, M + 1):
        if is_prime[i]:
            for j in range(i * 2, M + 1, i):
                is_prime[j] = 0
    
    for i in range(1, M + 1):
        is_prime[i] += is_prime[i - 1]
    
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        if n <= 3: outs.append(n - 2)
        else: outs.append(is_prime[n] - is_prime[n // 2])
    
    print('\n'.join(map(str, outs)))