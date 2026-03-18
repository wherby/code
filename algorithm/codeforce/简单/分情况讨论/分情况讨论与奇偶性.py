# https://codeforces.com/gym/106259/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0316/solution/cf106259a.md
# 分情况讨论特殊情况1 的时候，把所有对称情况合并
# 讨论奇偶性



import init_setting
from lib.cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n, m, r1, c1, r2, c2 = MII()
        
        if n % 2 and m % 2: outs.append('NO')
        elif fmin(n, m) == 1:
            if m == 1:
                n, m = m, n
                r1, c1 = c1, r1
                r2, c2 = c2, r2
            if c1 > c2: c1, c2 = c2, c1
            if (c1 - 1) % 2 or (c2 - c1 - 1) % 2 or (m - c2) % 2:
                outs.append('NO')
            else:
                outs.append('YES')
        elif (r1 + c1) % 2 == (r2 + c2) % 2: outs.append('NO')
        else: outs.append('YES')
    
    print('\n'.join(map(str, outs)))