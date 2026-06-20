# https://codeforces.com/gym/104395/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0620/solution/cf104395f.md
# 这里有个结论，无论添加的边是否构成环，最后剩余的开放的链的数量都是n-m
# 然后对于每增加一个链条。则它有 1/N 个概率自己连自己，刚好是环的期望数量
# algorithm/codeforce/概率/doc/期望的均匀性.md



import init_setting
from cflibs import *
from lib.UnionFind import *
from lib.combineWithPreCompute import * 
def main():
    n, m = MII()
    uf = UnionFind(n)
    
    mod = 10 ** 9 + 7
    f = Factorial(n, mod)
    
    ans = 0
    
    for _ in range(m):
        u, v = GMI()
        if not uf.merge(u, v):
            ans += 1
    
    for i in range(1, n - m + 1):
        ans += f.inv(i)
        ans %= mod
    
    print(ans)