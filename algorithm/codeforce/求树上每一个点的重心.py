# https://codeforces.com/problemset/problem/685/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/05/0505/solution/cf685b.md
# 求树上每个节点的重心，首先使用BFS获取访问顺序
# 使用递归方法，在访问顺序逆序处理，如果没有子树则重心在自身，否则，根节点的重心一定是最大子树的重心到根的路径上
# #TAG#TREE#重心

import sys
sys.path.append("..")
from cflibs.cflibs import *

def main():
    n, q = MII()
    parent = [-1] + LGMI()

    path = [[] for _ in range(n)]

    for i in range(1, n):
        path[parent[i]].append(i)

    que = [0]
    for u in que:
        for v in path[u]:
            que.append(v)

    sz = [1] * n

    for i in range(n - 1, 0, -1):
        u = que[i]
        p = parent[u]
        sz[p] += sz[u]

    centroid = [-1] * n

    for i in range(n - 1, -1, -1):
        u = que[i]
        if len(path[u]) == 0:
            centroid[u] = u
        else:
            v = -1
            for nv in path[u]:
                if v == -1 or sz[nv] > sz[v]:
                    v = nv
            v = centroid[v]
            while 2 * sz[v] < sz[u]:
                v = parent[v]
            centroid[u] = v

    outs = []
    for _ in range(q):
        outs.append(centroid[II() - 1] + 1)

    print('\n'.join(map(str, outs)))