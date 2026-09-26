# https://codeforces.com/gym/101055/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0922/solution/cf101055c.md
# 这里利用容斥原理，奇数个质素的平方数系数为负
# 从1 开始的时候，此时系数为正，正好符合全局减去容斥去除的个数


import init_setting
from cflibs import *
def main():
    M = 200000
    
    is_prime = [1] * M
    is_prime[0] = 0
    is_prime[1] = 0
    
    miu = [1] * M
    
    for i in range(M):
        if is_prime[i]:
            for j in range(i, M, i):
                is_prime[j] = 0
                miu[j] *= -1
                
                if j // i % i == 0:
                    miu[j] = 0
    
    chosen = [i for i in range(1, M) if miu[i]]
    
    t = II()
    outs = []
    
    for _ in range(t):
        x = II()
        
        l, r = 1, 4 * 10 ** 10
        while l <= r:
            mid = (l + r) // 2
            
            cnt = 0
            
            for i in chosen:
                cnt += miu[i] * (mid // i // i)
            
            if cnt >= x: r = mid - 1
            else: l = mid + 1
        
        outs.append(l)
    
    print('\n'.join(map(str, outs)))