# 这里有多维空间中选择最短路径，不能直接使用最短路径算法，由于有跳转数量限制，可以在每个空间先求出最短路径再DP
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/04/0415/solution/cf187b.md
# https://codeforces.com/problemset/problem/187/B

from cflibs import *
def main():
    n, m, q = MII()
    inf = 10 ** 6
    dis = [[[inf] * n for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        grid = [LII() for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    grid[j][k] = fmin(grid[j][k], grid[j][i] + grid[i][k])
        
        for i in range(n):
            for j in range(n):
                dis[0][i][j] = fmin(dis[0][i][j], grid[i][j])

    for i in range(1, n):
        for u in range(n):
            for v in range(n):
                for w in range(n):
                    dis[i][u][w] = fmin(dis[i][u][w], dis[i - 1][u][v] + dis[0][v][w])

    outs = []

    for _ in range(q):
        u, v, k = MII()
        u -= 1
        v -= 1
        outs.append(dis[fmin(k, n - 1)][u][v])

    print('\n'.join(map(str, outs)))