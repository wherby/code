# https://codeforces.com/gym/105198/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0127/solution/cf105198a.md
# 题意是计算一种特殊的SOS运算的结果，观察运算规则可以发现每一位上的结果是独立的，然后每一位上结果的计算可以通过k+1的幂次来表示
# 如果x只有一个1位， 则 f(k,x) = x, 如果x有两个1位，则 f(k,x) = x * (k + 1), 如果x有三个1位，则 f(k,x) = x * (k + 1)^2
# 可以发现每一位上1的个数是x的二进制表示中1的个数，然后每一位上结果是k+1的幂次乘以x中1的个数，因为SOS 运算的时候每多一位等于在前一个结果状态“多一层” 


import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    mod = 10 ** 9 + 7
    
    for _ in range(t):
        k, x = MII()
        outs.append(x * pow(k + 1, x.bit_count() - 1, mod) % mod)
    
    print('\n'.join(map(str, outs)))