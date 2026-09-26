# https://codeforces.com/gym/106642/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0812/solution/cf106642c.md
# 对每位进行清除再标记的方式进行差分维护，这样使得pos更新更加简单，清除掉再计算反而比维护一个状态集合更容易

import init_setting
from lib.cflibs import *

def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n, m, k = MII()
        nums = LII()
        
        def f(x):
            if x < 0:
                return 0
            
            ans = 0
            
            last_0 = [-1] * m
            last_1 = [-1] * m
            vis = [0] * n
            
            l = 0
            cur = 0
            
            for r in range(n):
                for i in range(m):
                    pos = fmin(last_0[i], last_1[i])
                    if l <= pos <= r:
                        cur -= 1
                    if pos >= 0:
                        vis[pos] -= 1
                    
                    if nums[r] >> i & 1:
                        last_1[i] = r
                    else:
                        last_0[i] = r
                    
                    pos = fmin(last_0[i], last_1[i])
                    if l <= pos <= r:
                        cur += 1
                    if pos >= 0:
                        vis[pos] += 1
                
                while cur > x:
                    cur -= vis[l]
                    l += 1
                
                ans += r - l + 1
            
            return ans
        
        outs.append(f(k) - f(k - 1))
    
    print('\n'.join(map(str, outs)))