# https://codeforces.com/gym/106247/problem/4
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0220/solution/cf106247d.md
# 求一个数与已知数的LCM最小，等价于求这个数与已知数的GCD最大

import init_setting
from cflibs import *

def main(): 
    n = II()
    k = II()
    
    ans = n + 1
    
    for i in range(1, 10 ** 6 + 1):
        if n % i == 0:
            if i <= k: ans = fmax(ans, n + i)
            if n // i <= k: ans = fmax(ans, n + n // i)
    
    print(ans)