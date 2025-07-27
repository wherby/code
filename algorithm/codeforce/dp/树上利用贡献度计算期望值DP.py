# https://codeforces.com/problemset/problem/101/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0725/solution/cf101d.md
# 要求树上的点DFS访问的第一次访问时间的期望值，
# 算法用反DFS序的方式求子树的期望值，然后把子树放入同一级访问中按照顺序加入父节点
# 考虑路径值，路径值需要下放到子节点，比较需要子节点的权重和子节点的节点数的比值
# 然后DP根据子节点访问顺序，计算各个子树对期望权重的贡献度
# weight[v]: 表示v节点的所有子树路径权重 再加上到v节点的路径权重
# dp[v]：表示子树所有节点的期望权重


import init_setting
from lib.cflibs import *
def main():
    n = II()
    path = [[] for _ in range(n)]

    us = []
    vs = []
    ws = []

    for i in range(n - 1):
        u, v, w = MII()
        u -= 1
        v -= 1
        us.append(u)
        vs.append(v)
        ws.append(w)
        path[u].append(i)
        path[v].append(i)

    parent = [-1] * n
    que = [0]

    for u in que:
        for eid in path[u]:
            v = us[eid] + vs[eid] - u
            if parent[u] != v:
                parent[v] = u
                que.append(v)

    sz = [1] * n
    szt = [0] * n
    dp = [0] * n
    weights = [0] * n

    def cmp(x, y):
        v1 = weights[x] * sz[y]
        v2 = weights[y] * sz[x]
        
        if v1 < v2: return -1
        if v1 > v2: return 1
        return 0

    for u in reversed(que):
        sons = []
        
        for eid in path[u]:
            v = us[eid] + vs[eid] - u
            w = ws[eid]
            
            if parent[v] == u:
                sons.append(v)
                weights[v] = w + szt[v]
                sz[u] += sz[v]
                szt[u] += w + szt[v]
                dp[u] += dp[v] + sz[v] * w
        
        sons.sort(key=cmp_to_key(cmp))
        
        total_sz = sz[u] - 1
        for v in sons:
            total_sz -= sz[v]
            dp[u] += weights[v] * total_sz * 2

    print(dp[0] / (n - 1))