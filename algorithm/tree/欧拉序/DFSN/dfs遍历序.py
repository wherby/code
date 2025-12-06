# https://codeforces.com/problemset/problem/1006/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/06/0614/solution/cf1006e.md
# DFS 不用双端队列的写法 
# 使用ord长度确定进入的时间，用反向ord遍历的方式把子节点的大小加到父节点，维护节点对于子树的大小

import sys
sys.path.append("..")
from cflibs.cflibs import *
def main():
    n, q = MII()
    parent = [-1] + LGMI()

    path = [[] for _ in range(n)]

    for i in range(1, n):
        path[parent[i]].append(i)

    for i in range(n):
        path[i].reverse()

    stk = [0]
    order = []
    pos = [-1] * n

    while stk:
        u = stk.pop()
        pos[u] = len(order)
        order.append(u)
        
        for v in path[u]:
            stk.append(v)

    sz = [1] * n
    for u in reversed(order):
        if u: sz[parent[u]] += sz[u]

    outs = []
    for _ in range(q):
        u, k = GMI()
        outs.append(order[pos[u] + k] + 1 if k < sz[u] else -1)

    print('\n'.join(map(str, outs)))