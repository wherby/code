# https://codeforces.com/problemset/problem/148/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0814/solution/cf148c.md
# 构造数列的时候，由于倍增B的情况比较难满足，所以需要先考虑b,然后再考虑a 

import init_setting
from lib.cflibs import *
def main():
    n, a, b = MII()
    
    if a and a == n - 1: print(-1)
    elif n == 1: print(1)
    else:
        ans = [1, 2]
        if b == 0: ans = [2, 1]
        else: b -= 1
        
        cur = 3
        for i in range(2, n):
            if b:
                b -= 1
                ans.append(cur + 1)
                cur = cur * 2 + 1
            elif a:
                a -= 1
                ans.append(fmax(ans[0], ans[-1]) + 1)
            else:
                ans.append(1)
        
        print(*ans)