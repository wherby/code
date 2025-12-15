# https://codeforces.com/gym/105863/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/12/1212/solution/cf105863g.md
# 全排列数组，第i个数字是最小的数字的期望和

import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    mod = 998244353
    
    for _ in range(t):
        n, k = MII()
        
        ans = n
        revk = pow(k, -1, mod)
        for i in range(1, k):
            prob = i * revk % mod
            ans += (1 - pow(prob, n, mod)) * pow(1 - prob, -1, mod)
            ans %= mod
        
        outs.append(ans * pow(k, n - 1, mod) % mod)
    
    print('\n'.join(map(str, outs)))

main() 