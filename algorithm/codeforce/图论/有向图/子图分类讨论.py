# https://codeforces.com/problemset/problem/859/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0709/solution/cf859e.md
# 有向图，每个点出度为1， 入度不确定，可以构成： 自环， 环， 基环树，树/链
# 对于自环，方案就只有1个， 基环树的时候，因为出度为1， 环上的点有两种选择，但是环上出去的点只能选择出去的位置，所以对应的链路是固定的， 环则也是两种选择
# 对于树/链，方案为联通块的数目， 用链路分析如下
# 1<-2<-3<4   : (4, 1<-2<-3) (1,2,3)
# 1<-2<-3     : (3, 1<-2).  (1,2)
# 1<-2.       : (2,).       (1)
# 对于树的分析，可以从根上来， 如果选择了根，就是迭代子树，如果不选根，则所有选择都固定，所以方案数目就是联通块节点数目
   
import sys
sys.path.append("..")
from cflibs.cflibs import *
def main():
    n = II()
    mod = 10 ** 9 + 7

    us = []
    vs = []

    for _ in range(n):
        u, v = GMI()
        us.append(u)
        vs.append(v)

    dsu = UnionFind(2 * n)

    for i in range(n):
        dsu.merge(us[i], vs[i])

    cnt = [0] * (2 * n)
    flg = [1] * (2 * n)

    for i in range(n):
        cnt[dsu.find(us[i])] += 1
        if us[i] == vs[i]:
            flg[dsu.find(us[i])] = 0

    ans = 1

    for i in range(2 * n):
        if dsu.find(i) == i and flg[i]:
            sz = dsu.getSize(i)
            if cnt[i] < sz: ans = ans * sz % mod
            else: ans = ans * 2 % mod

    print(ans)