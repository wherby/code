# https://codeforces.com/problemset/problem/141/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0905/solution/cf141e.md
# 原题是一个图N个节点里有M条边， 每条边有不同的属性，需要选择N-1条边把边按照属性均分之后组成最小生成树
# 利用两个DSU 巧妙解决，在两个空间作合并，第一个空间合并所以属性1 的边， 第二空间先合并第一空间的差集边，然后用边数量相等的特点，寻找替换边


import init_setting
from cflibs import *
from lib.UnionFind import * 
def main():
    n, m = MII()
    us = []
    vs = []
    cs = []
    
    for _ in range(m):
        u, v, c = LI()
        u = int(u) - 1
        v = int(v) - 1
        c = 1 if c == 'S' else 0
        us.append(u)
        vs.append(v)
        cs.append(c)
    
    if n % 2 == 0: exit(print(-1))
    
    target = n // 2
    ans = []
    
    uf_base = UnionFind(n)
    real_uf = UnionFind(n)
    
    for i in range(m):
        if cs[i] == 0:
            uf_base.merge(us[i], vs[i])
    
    for i in range(m):
        if cs[i] and uf_base.merge(us[i], vs[i]):
            real_uf.merge(us[i], vs[i])
            ans.append(i)
    
    for i in range(m):
        if len(ans) < target and cs[i] and real_uf.merge(us[i], vs[i]):
            ans.append(i)
    
    if len(ans) != target: exit(print(-1))
    
    for i in range(m):
        if cs[i] == 0 and real_uf.merge(us[i], vs[i]):
            ans.append(i)
    
    if len(ans) == n - 1:
        print(len(ans))
        print(' '.join(str(x + 1) for x in ans))
    else:
        print(-1)