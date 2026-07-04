# https://codeforces.com/gym/106607/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0703/solution/cf106607g.md
# 奇偶性和最大最小边界讨论


import init_setting
from lib.cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n, m, k = MII()
        ans = n

        if ans % 2 != k % 2:
            ans -= 1
        ans = fmin(ans, k)
        if m % 2 == 0:
            ans = fmin(ans, n * m - k)
    
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))