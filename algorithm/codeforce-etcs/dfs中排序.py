# https://codeforces.com/problemset/problem/29/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/04/0409/solution/cf29d.md

# 需要实现DFS中不一样的子节点遍历顺序: DFS遍历的顺序可以保证逆序 一定是从叶子到根的路径，利用这个遍历顺序，确定每个子节点的遍历优先级

from cflibs import *
def main():
    n = II()
    path = [[] for _ in range(n)]

    for _ in range(n - 1):
        u, v = GMI()
        path[u].append(v)
        path[v].append(u)

    is_leaf = [1] * n

    parent = [-1] * n
    que = [0]

    for u in que:
        for v in path[u]:
            if parent[u] != v:
                is_leaf[u] = 0
                parent[v] = u
                que.append(v)

    nodes = LGMI()
    k = len(nodes)

    vis = [n] * n
    for i in range(k):
        vis[nodes[i]] = i

    for i in range(n - 1, 0, -1):
        u = que[i]
        vis[parent[u]] = fmin(vis[parent[u]], vis[u])

    ans = []
    stk = [0]

    while stk:
        u = stk.pop()
        if u >= 0:
            if u > 0:
                ans.append(parent[u])
            stk.append(~u)
            path[u].sort(key=lambda x: -vis[x])
            for v in path[u]:
                if parent[v] == u:
                    stk.append(v)
        else:
            ans.append(~u)

    pt = 0
    for u in ans:
        if pt < k and nodes[pt] == u:
            pt += 1

    if pt == k: print(' '.join(str(x + 1) for x in ans))
    else: print(-1)