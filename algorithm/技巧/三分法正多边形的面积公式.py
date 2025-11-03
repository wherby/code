# https://codeforces.com/gym/106157/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1103/solution/cf106157e.md
# 枚举计算正多边形的周长，通过边长计算正多变性的面积
# 三分法求极值

import init_setting
from lib.cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        m, t = MII()
        
        if t <= 3 * m: outs.append(0)
        else:
            l, r = 3, t // m
            
            def f(x):
                side = (t / x - m) / 2
                return side * side / math.tan(math.pi / x) * x
            
            while l < r:
                mid = (l + r) // 2
                if f(mid) < f(mid + 1):
                    l = mid + 1
                else:
                    r = mid
            
            outs.append(f(l))
    
    print('\n'.join(map(str, outs)))