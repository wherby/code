# https://codeforces.com/gym/106296/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0110/solution/cf106296c.md
# 因为 b一定有重复点，而b1=a2 所以可以用查询区域是否一定重复来二分判断重复点的区间

import init_setting
from lib.cflibs import *
def main(): 
    def check(x):
        print(2, 2 * x - 1, flush=True)
        v1 = II()
        print(1, 2 * x, flush=True)
        v2 = II()
        return v1 == v2
    
    t = II()
    
    for _ in range(t):
        n = II()
        v = (n + 1) // 2
        
        l, r = 1, v - 1
        while l <= r:
            mid = (l + r) // 2
            
            if check(mid): l = mid + 1
            else: r = mid - 1
        
        print(3, 2 * r - 1, 2 * r + 1, flush=True)