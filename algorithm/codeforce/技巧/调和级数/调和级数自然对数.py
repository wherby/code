# https://codeforces.com/gym/104012/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1015/solution/cf104012g.md
# 这里需要枚举所有可能的情况
# 这里枚举y, 对于一个y而言 x//y 的值是一个调和级数
# 而同样，对于求出的g 而言， y 与g 整除的情况也有调和倍数衰减， 在枚举x的时候，也需要用g调和倍数跳跃减少枚举数量

import init_setting
from cflibs import *
def main():
    n, q = MII()
    
    def f(x, y):
        return x if y == 0 else f(y, x // y)
    
    tmp = [[] for _ in range(n + 1)]
    
    for i in range(2, n + 1):
        for j in range(1, n // i + 1):
            g = f(i, j)
            
            if i % g == 0:
                l = i * j
                r = fmin(i * (j + 1), n + 1)
                
                for v in range(((l - 1) // g + 1) * g, r, g):
                    if math.gcd(v, i) == g:
                        tmp[v].append(i)
    
    res = []
    
    for i in range(n + 1):
        for j in tmp[i]:
            res.append(i * (n + 1) + j)
    
    outs = []
    
    for _ in range(q):
        p = II()
        
        if p <= len(res):
            x, y = divmod(res[p - 1], n + 1)
            outs.append(f'{x} {y}')
        else:
            outs.append('-1 -1')
    
    print('\n'.join(outs))