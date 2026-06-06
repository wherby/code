# https://codeforces.com/gym/106523/problem/M
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0601/solution/cf106523m.md
# 使用不动点特点二分求期望值

import init_setting
from cflibs import *
def main():
    n = II()
    ds = LII()
    probs = LFI()
    
    l, r = 0, 10 ** 9
    
    for _ in range(100):
        mid = (l + r) / 2
        cur = mid
        
        for i in range(n - 1, -1, -1):
            cur = probs[i] * fmin(cur + 1, ds[i]) + (1 - probs[i]) * (cur + 1)
    
        if cur < mid: r = mid
        else: l = mid
    
    print((l + r) / 2)