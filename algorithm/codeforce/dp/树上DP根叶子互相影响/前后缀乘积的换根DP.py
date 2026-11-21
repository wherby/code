# https://codeforces.com/gym/106826/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/11/1116/solution/cf106826b.md
# 这里用0 作为根节点，有可能不是符合二叉树定义，但是这里不会影响结果，只是先求出每个分叉的值
# 换根的时候用 rev_dp 表示出去当前子树外的剩余子树的结果
# 组合再用  if len(path[i]) <= 2:  移除了不能当根节点的节点，然后合并前后缀(即子树和子树外部分)


import init_setting
from lib.cflibs import *


def main():
    t = II()
    outs = []
    mod = 998244353

    for _ in range(t):
        n = II()
        path = [[] for _ in range(n)]

        for _ in range(n - 1):
            u, v = GMI()
            path[u].append(v)
            path[v].append(u)

        parent = [-1] * n
        que = [0]

        for u in que:
            for v in path[u]:
                if parent[u] != v:
                    parent[v] = u
                    que.append(v)

        dp = [1] * n

        for u in reversed(que):
            tmp = []

            for v in path[u]:
                if parent[v] == u:
                    tmp.append(v)

            if len(tmp) == 3:
                dp[u] = 0
                continue

            elif len(tmp):
                dp[u] = 2
                for v in tmp:
                    dp[u] = dp[u] * dp[v] % mod

        rev_dp = [1] * n

        for u in que:
            if u == 0:
                if len(path[u]) == 1:
                    rev_dp[path[u][0]] = rev_dp[u]

                else:
                    for x in path[0]:
                        rev_dp[x] = 2
                        for y in path[0]:
                            if y != x:
                                rev_dp[x] = rev_dp[x] * dp[y] % mod
            else:
                sons = []
                for v in path[u]:
                    if parent[v] == u:
                        sons.append(v)

                for x in sons:
                    rev_dp[x] = 2 * rev_dp[u] % mod
                    for y in sons:
                        if y != x:
                            rev_dp[x] = rev_dp[x] * dp[y] % mod

        ans = 0
        for i in range(n):
            if len(path[i]) <= 2:
                res = 2 * rev_dp[i] % mod
                for j in path[i]:
                    if parent[j] == i:
                        res = res * dp[j] % mod
                ans = (ans + res) % mod

        outs.append(ans)

    print("\n".join(map(str, outs)))


# 这个题目可以用度来解决

import sys


def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return

    n = int(data[0])
    if n == 1:
        print(1)
        return

    deg = [0] * (n + 1)
    idx = 1
    for _ in range(n - 1):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        deg[u] += 1
        deg[v] += 1

    n1 = 0
    n2 = 0
    k = 0
    for i in range(1, n + 1):
        if deg[i] == 1:
            n1 += 1
        elif deg[i] == 2:
            n2 += 1
        if deg[i] >= 2:
            k += 1

    MOD = 998244353
    ans = (n1 * pow(2, k + 1, MOD) + n2 * pow(2, k, MOD)) % MOD
    print(ans)


if __name__ == "__main__":
    solve()
