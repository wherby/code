# https://codeforces.com/gym/105390/problem/C2
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0108/solution/cf105390c2.md
# 原题化简为 在所有偶数中间都有奇数的排列数有多少个
# 对于N==偶数， 则偶数中先插入一个奇数，则先消耗了 N//2-1 个奇数，剩余一个奇数可以插入到 N//2+1个空位中
# 对于N==奇数， 则消耗了N//2-1个奇数的时候，剩余了两个奇数可以插入 N//2 +1 个空位中
# algorithm/mathA/combination/N球M盒问题.md

import init_setting
from cflibs import *
def main(): 
    M = 3 * 10 ** 5
    mod = 10 ** 9 + 7
    
    f = [0] * (M + 1)
    f[0] = 1
    
    for i in range(1, M + 1):
        f[i] = i * f[i - 1] % mod
    
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        ans = f[n // 2] * f[n - n // 2] % mod
        if n % 2 == 0: ans = ans * (n // 2 + 1) % mod
        else: ans = ans * ((n // 2 + 1) * (n // 2 + 2) // 2 % mod) % mod
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))