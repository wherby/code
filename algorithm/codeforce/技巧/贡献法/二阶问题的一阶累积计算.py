# https://codeforces.com/gym/105059/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/05/0529/solution/cf105059f.md
# 对于任意窗口的平均数的平均数
# 采用同一长度的窗口平均数和一起计算的方式，采用了窗口累积的算法，随着长度增加，正负项累积计算，实现了降维操作
# algorithm/codeforce/技巧/贡献法/docs/窗口累积算法.md

import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        nums = LII()
        
        ans = 0
        
        acc = list(accumulate(nums, initial=0))
        
        cur = 0
        
        for i in range(n):
            cur += acc[n - i] - acc[i]
            ans += cur / (i + 1)
        
        outs.append(ans / (n * (n + 1) / 2))
    
    print('\n'.join(map(str, outs)))