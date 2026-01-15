# https://codeforces.com/gym/104287/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0105/solution/cf104287f.md
# 裴蜀定理，可以找到一个系数，使得 kV mod C = gcd(V,c)

import init_setting
from lib.cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        a, b, c = MII()
        outs.append(c - math.gcd(c, math.lcm(a, b)))
    
    print('\n'.join(map(str, outs)))