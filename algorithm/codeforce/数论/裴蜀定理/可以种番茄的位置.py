# https://codeforces.com/gym/106189/problem/I
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1115/solution/cf106189i.md
# 这里有两个问题，可以跳跃的距离 x,y 可以用平方根方式遍历
# 跳跃的时候，最小间隔是 gcd *2 ,因为是对角上跳跃，则分别从（0,0），（g,g)出发。寻找里面落脚点个数

import init_setting
from cflibs import *    
def main(): 
    n, xl, yl, w, h = MII()
    xr, yr = xl + w, yl + h
    xl, yl = xl - 1, yl - 1
    
    g = 0
    
    for i in range(1, 10 ** 6 + 1):
        v = n - i * i
        if v < 0: break
        w = math.isqrt(v)
        if i > w: break
        if w * w == v:
            g = math.gcd(g, i)
            g = math.gcd(g, w)
    
    ans = 0
    if g:
        ans += (xr // (2 * g) - xl // (2 * g)) * (yr // (2 * g) - yl // (2 * g))
        ans += ((xr - g) // (2 * g) - (xl - g) // (2 * g)) * ((yr - g) // (2 * g) - (yl - g) // (2 * g))
    elif xl < 0 <= xr and yl < 0 <= yr:
        ans += 1
    
    print(ans)