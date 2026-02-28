# https://codeforces.com/gym/103870/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0225/solution/cf103870g.md
# 打表找规律

import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        l, r, m = MII()
        v = 1 << m.bit_length() - 1
        outs.append((r + 1) // v - l // v)
    
    print('\n'.join(map(str, outs)))