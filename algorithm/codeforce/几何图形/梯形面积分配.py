# 
# 
# https://codeforces.com/gym/106369/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0218/solution/cf106369f.md
# 不知道怎么分配，就固定x，然后就可以得到上下三角形和中间平分的面积，然后用三分发找到最优的x

import init_setting
from lib.cflibs import *
def main(): 
    b1, b2, h = MII()
    
    def f(x):
        tmp = [b1 * x, b2 * (h - x), ((b1 + b2) * h - b1 * x - b2 * (h - x)) / 2]
        return max(tmp) - min(tmp)
    
    l, r = 0, h
    
    for _ in range(100):
        mid1 = (l * 2 + r) / 3
        mid2 = (l + r * 2) / 3
        
        if f(mid1) < f(mid2): r = mid2
        else: l = mid1
    
    print(f((l + r) / 2) / 2)