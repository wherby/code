# https://codeforces.com/problemset/problem/15/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0825/solution/cf15b.md
# 求的面积就是全面积减去两个可能会重叠的移动面积  【也等价于用两个可能重叠的不被覆盖的面积之和】
#

import init_setting
from lib.cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n, m, x1, y1, x2, y2 = MII()
        
        if x1 > x2: x1, x2 = x2, x1
        if y1 > y2: y1, y2 = y2, y1
        
        a = x1 + n - x2
        b = y1 + m - y2
        outs.append(n * m - 2 * a * b + fmax(0, a * 2 - n) * fmax(0, b * 2 - m))
    
    print('\n'.join(map(str, outs)))