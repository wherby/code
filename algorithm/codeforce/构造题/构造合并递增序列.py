# https://codeforces.com/problemset/problem/207/A3
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0908/solution/cf207a3.md
# 需要合并多个顺序序列，变成最少分段的递增序列
# 合并每段的递增序列，就能取得最少得递增序列分段数

import init_setting
from lib.cflibs import *
def main():
    n = II()
    ks = [0] * n
    a1s = [0] * n
    xs = [0] * n
    ys = [0] * n
    ms = [0] * n
    
    for i in range(n):
        ks[i], a1s[i], xs[i], ys[i], ms[i] = MII()
    
    sumk = sum(ks)
    tmp = [[] for _ in range(200005)]
    
    def f(i, j):
        return i * n + j
    
    ans = 0
    
    for i in range(n):
        k = ks[i]
        a = a1s[i]
        x = xs[i]
        y = ys[i]
        m = ms[i]
        
        vs = [a]
        
        for _ in range(1, k):
            a = (a * x + y) % m
            vs.append(a)
        
        c = 0
        for j in range(k):
            if j and vs[j] < vs[j - 1]:
                c += 1
            if sumk <= 200000:
                tmp[c].append(f(vs[j], i))
        
        ans = fmax(ans, c)
    
    print(ans)
    
    if sumk <= 200000:
        outs = []
        
        for x in tmp:
            x.sort()
            for v in x:
                val, idx = divmod(v, n)
                outs.append(f'{val} {idx + 1}')
        
        print('\n'.join(outs))