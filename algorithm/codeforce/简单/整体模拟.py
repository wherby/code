# https://codeforces.com/gym/100947/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0929/solution/cf100947c.md
# 基于长度为奇数和偶数，把左移的过程中，序列和作为一个整体模拟

import init_setting
from lib.cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        nums = LII()
    
        ans = -inf
        
        v0, v1 = sum(nums[::2]), sum(nums[1::2])
        
        for i in range(n):
            v0, v1 = v1, v0 - nums[i]
            if n % 2: v0 += nums[i]
            else: v1 += nums[i]
            
            ans = fmax(ans, v0)
        
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))