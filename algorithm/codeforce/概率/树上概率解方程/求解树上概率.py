# https://codeforces.com/problemset/problem/802/L
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0712/solution/cf802l.md
# 求解树上移动的平均概率
# 如果移动在叶子节点则停止，否则概率平均移动到相邻节点，解法用了数的从叶子到根的递归。
# 因为求当前节点cost的时候，需要知道根节点的cost，这与递归方向矛盾
# algorithm/codeforce/概率/树上概率解方程/Google Gemini.pdf
# 边界限定的波动方程解法？

import sys
sys.path.append("..")
from cflibs.cflibs import *
def main():
    n = II()
    mod = 10 ** 9 + 7
    path = [[] for _ in range(n)]

    us = []
    vs = []
    cs = []

    for i in range(n - 1):
        u, v, c = MII()
        path[u].append(i)
        path[v].append(i)
        
        us.append(u)
        vs.append(v)
        cs.append(c)

    parent = [-1] * n

    que = [0]
    for u in que:
        for eid in path[u]:
            if parent[u] != eid:
                v = us[eid] + vs[eid] - u
                parent[v] = eid
                que.append(v)

    ks = [0] * n
    bs = [0] * n

    for u in reversed(que):
        if len(path[u]) == 1 and u > 0: continue
        
        sumk = 0
        sumb = 0
        sumc = 0
        
        for eid in path[u]:
            v = us[eid] + vs[eid] - u
            sumc += cs[eid]
            if parent[v] == eid:
                sumk += ks[v]
                sumb += bs[v]
        
        rev = pow(len(path[u]) - sumk, -1, mod)
        ks[u] = rev
        bs[u] = (sumb + sumc) * rev % mod

    print(bs[0])