# https://codeforces.com/gym/106033/problem/I
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/12/1211/solution/cf106033i.md
# 由于有两个自由运动a,b 和一个约束,把两个自由运动合成为一个在数轴上的自由运动，
# 然后用反射原理求取自由路径值和反射后的自由路径值，相减，化简等式



import init_setting
from cflibs import *
from lib.combineWithPreCompute import Factorial

def main(): 
    n, k = MII()
    n -= 1
    mod = 998244353
    
    f = Factorial(2 * n, mod)
    
    ans = 0
    for i in range(n - k - 1, n + k + 1):
        ans += f.comb(2 * n, i)
        ans %= mod
    
    print(ans)
main()