# https://codeforces.com/gym/104669/problem/L
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0303/solution/cf104669l.md
# 数组和的因子包含数组元素的GCD - 数组和的因子包含数组元素的GCD，说明数组元素的GCD一定是数组和的因子
# 反过来说，如果数组元素的GCD是数组和的因子，那么数组元素的GCD一定包含在数组和的因子中，所以满足条件

import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        a, b = MII()
        total = (2 * a + b - 1) * b // 2
        
        def check(x):
            for i in range(1, b):
                l = a * i + i * (i - 1) // 2
                r = a * i + (2 * b - 1 - i) * i // 2
                if r // x * x >= l: return True
            return False
        
        ans = 0
        for i in range(1, 10 ** 5 * 2):
            if i * i > total: break
            if total % i == 0:
                if check(i): ans = fmax(ans, i)
                if check(total // i): ans = fmax(ans, total // i)
        
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))