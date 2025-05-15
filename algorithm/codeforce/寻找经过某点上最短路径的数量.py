# https://codeforces.com/problemset/problem/208/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/05/0513/solution/cf208c.md
# 寻找经过某点的最短路径数量 -》 从起始点 和结束点 求最短路径，用queue记录 访问顺序，再在最短路径上做dp计数

from cflibs import *
def main():
    n, m = MII()
    path = [[] for _ in range(n)]

    for _ in range(m):
        u, v = GMI()
        path[u].append(v)
        path[v].append(u)

    dis1 = [-1] * n
    dis1[0] = 0
    que = [0]

    for u in que:
        for v in path[u]:
            if dis1[v] == -1:
                dis1[v] = dis1[u] + 1
                que.append(v)


    dp1 = [0] * n
    dp1[0] = 1

    for u in que:
        for v in path[u]:
            if dis1[v] + 1 == dis1[u]:
                dp1[u] += dp1[v]

    disn = [-1] * n
    disn[n - 1] = 0
    que = [n - 1]

    for u in que:
        for v in path[u]:
            if disn[v] == -1:
                disn[v] = disn[u] + 1
                que.append(v)

    dpn = [0] * n
    dpn[n - 1] = 1

    for u in que:
        for v in path[u]:
            if disn[v] + 1 == disn[u]:
                dpn[u] += dpn[v]

    ans = dp1[n - 1]

    for i in range(1, n - 1):
        if dis1[i] + disn[i] == dis1[n - 1]:
            ans = fmax(ans, dp1[i] * dpn[i] * 2)

    print(ans / dp1[n - 1])