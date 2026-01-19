# https://codeforces.com/gym/103575/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0119/solution/cf103575b.md
# 利用两个UnionFind 记录不同类型对的边
# 偶数是非重要边，把所有偶数边都连上之后，查找奇数边的必须边，如果边数是奇数，则在奇数图上找打一个可以替代偶数边的边即可
# 利用两个UnionFind 记录了偶数非重要边，和的重要边分布情况




import init_setting
from cflibs import *
from lib.UnionFind import *

def main(): 
    n, m = MII()
    us = []
    vs = []
    ws = []
    
    for _ in range(m):
        u, v, w = MII()
        u -= 1
        v -= 1
        us.append(u)
        vs.append(v)
        ws.append(w)
    
    uf1 = UnionFind(n)
    uf2 = UnionFind(n)
    
    for i in range(m):
        if ws[i] % 2 == 0:
            uf1.merge(us[i], vs[i])
    
    used = [0] * m
    even = 1
    
    for i in range(m):
        if ws[i] % 2 and uf1.merge(us[i], vs[i]):
            uf2.merge(us[i], vs[i])
            used[i] = 1
            even ^= 1
    
    if not even:
        for i in range(m):
            if ws[i] % 2 and not used[i] and uf2.merge(us[i], vs[i]):
                used[i] = 1
                even ^= 1
                break
    
    if not even: print('NO')
    else:
        for i in range(m):
            if ws[i] % 2 == 0 and uf2.merge(us[i], vs[i]):
                used[i] = 1
        
        print('YES')
        print(' '.join(str(i + 1) for i in range(m) if used[i]))