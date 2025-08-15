# https://codeforces.com/problemset/problem/271/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0815/solution/cf271e.md
# 这里的三个变换对(x,y)只差产生的影响是什么，对应的最小元应该怎么求。
#  g //= g & -g 求得gcd的最大奇因子，
# 而g 可以由 它的任意因子合成，所以在solve里对因子求倍增，因为倍增是2的倍数，所以各个因子的倍增不会重叠，

import init_setting
from cflibs import *
def main():
    n, m = MII()
    nums = LGMI()
    
    g = math.gcd(*nums)
    g //= g & -g
    
    ans = 0
    
    def solve(x):
        res = 0
        v = x
        while v <= m:
            res += m - v
            v *= 2
        return res
    
    for i in range(1, 100000):
        if i > g // i: break
        
        if g % i == 0:
            ans += solve(i)
            if i != g // i:
                ans += solve(g // i)
    
    print(ans)