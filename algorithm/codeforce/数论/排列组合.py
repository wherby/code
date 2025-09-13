# https://codeforces.com/gym/103114/problem/H
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0909/solution/cf103114h.md
# 先查看有多少个空位，然后N个人，其实是在M-N个空位中查找N-1个数做隔离
# 第一个人可以放M个位置，然后还有N-1! 个组合

import init_setting
from cflibs import *
from lib.combineWithPreCompute import Factorial
def main():
    mod = 10 ** 9 + 7
    f = Factorial(10 ** 5, mod)
    
    t = II()
    outs = []
    
    for _ in range(t):
        n, m = MII()
        
        if n == m == 1:
            outs.append(1)
        elif 2 * n <= m:
            ans = m
            # x1 + x2 + ... + xn = n - m
            ans = ans * f.combi(m - n - 1, n - 1) % mod
            ans = ans * f.fac(n - 1) % mod
            outs.append(ans)
        else:
            outs.append(0)
    
    print(*outs, sep='\n')