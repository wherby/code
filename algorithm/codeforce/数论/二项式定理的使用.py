# https://codeforces.com/problemset/problem/2077/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0829/solution/cf2077c.md
# 二项式定义验证： algorithm/codeforce/数论/test/测试二项式定理.py
# rev4 这里有模数技巧 “模逆元”  使得 -1 和 -pw2[n-1] 除4 同余 
# (c0 * (c0 + 1) // 2 + c1 * (c1 + 1) // 2 - c0 * c1 - 1) 把 -1 移到了括号里面
# 二项式求和乘系数的化简 

import init_setting
from cflibs import *
def main():
    mod = 998244353
    
    M = 2 * 10 ** 5
    pw2 = [1] * (M + 1)
    
    for i in range(1, M + 1):
        pw2[i] = 2 * pw2[i - 1] % mod
    
    t = II()
    outs = []
    
    rev4 = ((mod + 1) // 2 + mod) // 2
    
    for _ in range(t):
        n, q = MII()
        s = [int(c) for c in I()]
        c0 = s.count(0)
        c1 = s.count(1)
        
        for _ in range(q):
            idx = II() - 1
            
            if s[idx]:
                c1 -= 1
                c0 += 1
            else:
                c1 += 1
                c0 -= 1
            
            s[idx] ^= 1
            
            outs.append((c0 * (c0 + 1) // 2 + c1 * (c1 + 1) // 2 - c0 * c1 - 1) * pw2[n - 1] % mod * rev4 % mod)
    
    print('\n'.join(map(str, outs)))