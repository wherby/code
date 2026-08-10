# https://codeforces.com/gym/106632/problem/K
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0804/solution/cf106632k.md
# 首先把计算的函数变形为统一参数的计算
# 然后得到函数是单调的，所以可以用二分计算单调区间内恰好等于k的个数
# 差分理解中，这里并没有采用二分查找得到区间，而是用两次小于等于的计算得到整体的差分个数

import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n, m = MII()
        nums = LII()
        
        def f(x):
            if x < 0: return 0
            
            l = 0
            r = 0
            
            cur_sum = 0
            cur_xor = 0
            
            ans = 0
            
            while l < n:
                r = fmax(l, r)
                
                while cur_sum - cur_xor <= x and r < n:
                    if r < n - 1:
                        v = nums[r] ^ nums[r + 1]
                        cur_sum += v
                        cur_xor ^= v
                    r += 1
                
                ans += r - l
                
                if l < n - 1:
                    v = nums[l] ^ nums[l + 1]
                    cur_sum -= v
                    cur_xor ^= v
                
                l += 1
            
            return ans
        
        outs.append(f(m) - f(m - 1))
    
    print('\n'.join(map(str, outs)))