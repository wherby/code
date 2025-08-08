# https://codeforces.com/problemset/problem/269/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0806/solution/cf269a.md

import init_setting
from cflibs import *
def main():
    n = II()
    ans = 0
    
    for _ in range(n):
        k, a = MII()
        
        ans = fmax(ans, k + 1)
        
        while a > 1:
            a = (a + 3) // 4
            k += 1
        
        ans = fmax(ans, k)
    
    print(ans)