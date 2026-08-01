# https://codeforces.com/gym/102767/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0722/solution/cf102767f.md

import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n, x = MII()
        nums = LII()
        
        mod_inv = [0] * x
        mod_inv[1] = 1
        
        for i in range(2, x):
            mod_inv[i] = mod_inv[x % i] * (x - x // i) % x
        
        ans = 0
        cur_len = 0
        
        vis = [-2] * x
        vis[1] = -1
        
        cur = 1
        
        for i in range(n):
            cur = cur * nums[i] % x
            
            for j in range(x):
                if vis[j] != -2 and (cur * mod_inv[j] % x > ans or (cur * mod_inv[j] % x == ans and i - vis[j] < cur_len)):
                    ans = cur * mod_inv[j] % x
                    cur_len = i - vis[j]
            
            vis[cur] = i
        
        outs.append(f'{ans} {cur_len}')
    
    print('\n'.join(outs))