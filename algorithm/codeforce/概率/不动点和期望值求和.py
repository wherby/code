# https://codeforces.com/gym/102129/problem/H
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0828/solution/cf102129h.md
# 因为 n 到去穷的时候，期望值应该是稳定的，所以是不动点，然后期望的分段求和就是两段等差数列求和
# algorithm/codeforce/概率/doc/期望的分段求和推导.md
# 这里先计算 V 的估计值(利用不动点构建方程)，然后验证左右值，找到正确的值, 然后再求真正的期望值， if k == m: continue 这时会有除0错误


import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    mod = 10 ** 9 + 7
    
    for _ in range(t):
        m = II()
        v = (2 * m + 1 - math.isqrt(2 * m * m + 2 * m + 1)) // 2
        
        for k in range(v - 1, v + 1):
            if k == m: continue
            A = m * m + m - 2 * (k * k + k)
            B = 4 * (m - k)
            
            if A // B == k:
                outs.append(A * pow(B, -1, mod) % mod)
                break
    
    print('\n'.join(map(str, outs)))