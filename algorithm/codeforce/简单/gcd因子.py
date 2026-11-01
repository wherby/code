# https://codeforces.com/gym/106795/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1031/solution/cf106795e.md
#

import init_setting
from lib.cflibs import *
def main(): 
    n, r = MII()
    
    t, c = MII()
    
    g = 0
    mx = c
    
    for _ in range(n - 1):
        nt, nc = MII()
        
        g = math.gcd(g, (nt - t) * r - (nc - c))
        mx = max(mx, nc)
    
    if g == 0: print(mx + 1)
    else:
        ans = inf
        for i in range(1, 10 ** 6 + 5):
            if g % i == 0:
                if i > mx: ans = fmin(ans, i)
                if g // i > mx: ans = fmin(ans, g // i)
        
        print(ans if ans < inf else -1)