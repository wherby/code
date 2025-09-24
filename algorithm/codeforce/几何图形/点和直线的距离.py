# https://codeforces.com/gym/105552/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0924/solution/cf105552d.md
# 点到直线的距离就是把点带入直线方程，求截距 abs(A*x + B*y + c) /sqrt(A**2 + B**2)
# 


import init_setting
from lib.cflibs import *
def main():
    n, r = MII()
    
    mi_d = r
    
    for _ in range(n):
        a, b, c = MII()
        d = abs(c) / math.sqrt(a * a + b * b)
        mi_d = fmin(d, mi_d)
    
    theta = math.acos(mi_d / r)
    
    v1 = theta - math.sin(theta) * math.cos(theta)
    v1 /= math.pi
    print(v1, 1 - v1)