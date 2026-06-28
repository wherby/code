# https://codeforces.com/gym/106020/problem/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0626/solution/cf106020j.md
# 分情况讨论，如果是 k & -k == k 表示k是2的幂次，
# 另外的情况是在1,2交替序列的时候，2 不够和 刚好剩余1的情况


import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n, k = MII()
        
        if n == 2:
            if k & -k == k: outs.append(1)
            else: outs.append(0)
        else:
            v = k - n
            if n % 2 == 0 and k - n == n // 2 + 1: outs.append(1)
            else: outs.append(fmax(0, n - 1 - 2 * v))
    
    print('\n'.join(map(str, outs)))