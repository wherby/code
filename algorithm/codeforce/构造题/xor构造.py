# https://codeforces.com/gym/104770/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0103/solution/cf104770d.md
# 

import init_setting
from cflibs import *
def main(): 
    n, m, k = MII()
    deg = [0] * (n + 1)
    outs = []
    
    for _ in range(m + k):
        u, v = MII()
        deg[u] ^= 1
        deg[v] ^= 1
        if u > 1 and v > 1:
            outs.append(f'1 {u} {v}')
    
    if max(deg): print('NO')
    else:
        print('YES')
        print(len(outs))
        print('\n'.join(outs))