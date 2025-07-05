# https://codeforces.com/problemset/problem/990/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/05/0531/solution/cf990f.md
# ？？首先液体流动的图里标注了每个点的净值，则这个图可以变为简单树形
# 把构造图的边权问题，转为树的边权问题，则可以用树的逆序遍历得到从叶子到根节点的所有边权值


import sys
sys.path.append("..")
from cflibs.cflibs import *
from lib.UnionFind import UnionFind
def main():
    n = II()
    nums = LII()

    m = II()

    us = []
    vs = []

    path = [[] for _ in range(n)]
    dsu = UnionFind(n)

    for i in range(m):
        u, v = GMI()
        us.append(u)
        vs.append(v)
        
        if dsu.merge(u, v):
            path[u].append(i)
            path[v].append(i)

    parent = [-2] * n
    ans = [0] * m

    for i in range(n):
        if parent[i] == -2:
            parent[i] = -1
            
            que = [i]
            for u in que:
                for eid in path[u]:
                    v = us[eid] + vs[eid] - u
                    if parent[u] != v:
                        parent[v] = u
                        que.append(v)
            
            for j in range(len(que) - 1, 0, -1):
                u = que[j]
                p = parent[u]
                nums[p] += nums[u]
                
                for eid in path[u]:
                    v = us[eid] + vs[eid] - u
                    if v == p:
                        if us[eid] == u: ans[eid] = -nums[u]
                        else: ans[eid] = nums[u]

            if nums[i]:
                exit(print('Impossible'))

    print('Possible')
    print(*ans, sep='\n')