# https://codeforces.com/gym/106174/problem/3
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1108/solution/cf106174c.md
# 窗口固定的线段和 有单调性，则可以二分，

import init_setting
from cflibs import *
def main(): 
    def f(x):
        start = 1
        d = 1
        ans = 0
        
        for _ in range(18):
            if start > x: break
            ans += fmin(start * 9, x - start + 1) * d
            start *= 10
            d += 1
        
        return ans
    
    n = II()
    k = II()
    
    l, r = 1, 10 ** 18
    
    while l <= r:
        mid = (l + r) // 2
        
        if f(mid + n - 1) - f(mid - 1) < k: l = mid + 1
        else: r = mid - 1
    
    print(l if f(l + n - 1) - f(l - 1) == k else -1)