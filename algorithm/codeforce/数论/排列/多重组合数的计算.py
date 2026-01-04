# https://codeforces.com/gym/104468/problem/M
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0102/solution/cf104468m.md
# 题目中的S是允许下降的位置的集合， 如果S是下降位置的集合，则问题会更困难
# 因为S是允许下降位置的集合，则问题变成，把N 个不同的数字分成了 M 段，每段内部是顺序排列的，段间的顺序不关心，这就是多重组合数
# 因为各个块是无关的，递推的的时候可以从最后一个块开始递推公式



import init_setting
from cflibs import *
def main(): 
    mod = 10 ** 9 + 7
    M = 2 * 10 ** 5
    f = Factorial(M, mod)
    
    t = II()
    outs = []
    
    for _ in range(t):
        n, k = MII()
        pos = [1] * (n - 1)
        
        for x in LGMI():
            pos[x] = 0
        
        ans = f.fac(n)
        
        cur = 1
        for x in pos:
            if x: cur += x
            else:
                ans = ans * f.fac_inv(cur) % mod
                cur = 1
        
        ans = ans * f.fac_inv(cur) % mod
        
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))