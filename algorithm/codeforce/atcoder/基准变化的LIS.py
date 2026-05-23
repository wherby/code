# https://atcoder.jp/contests/arc219/tasks/arc219_f
# https://atcoder.jp/contests/arc219/editorial/20151
# 题目中求最小的块操作选择奇偶性一致的块去除最低位使得数组全0
# 对于相邻的数字，如果成块的话，节约的操作对应与两个数的二进制LCS
# 但是变成0之后也可以与后面的数字组合，所以需要在前面补0计算，
# 而每次相邻的补零操作会有累积效应，所以DP的时候，需要预计补 L 个零
# 在转移的时候，根据不同的补零长度，从不同的转移计算得到


import sys

input = sys.stdin.readline
M = 60
INF = 10**9


def f(s: str, t: str):
    s += "0" * M
    n, m = len(s), len(t)
    d = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                d[i + 1][j + 1] = d[i][j] + 1
            else:
                d[i + 1][j + 1] = max(d[i][j + 1], d[i + 1][j])
    ans = []
    for i in range(n - M, n + 1):
        ans.append(d[i][m])
    return ans


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = ["" if x == 0 else bin(x)[2:][::-1] for x in a]
    L = M * (n + 1) + 1
    d = [j for j in range(L)]
    for i in range(n - 1):
        dd = [INF] * L
        r1 = f(s[i], s[i + 1])
        r2 = f(s[i + 1], s[i])
        for j1 in range(L):
            for j2 in range(L):
                if j1 < j2:
                    dd[j2] = min(dd[j2], d[j1] + j2 - j1 - r2[min(M, j2 - j1)])
                else:
                    dd[j2] = min(dd[j2], d[j1] + j2 - j2 - r1[min(M, j1 - j2)])
        d = dd
    print(sum(len(x) for x in s) + min(d))
