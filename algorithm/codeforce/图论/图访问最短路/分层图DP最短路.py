# https://codeforces.com/gym/104381/problem/L
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1020/solution/cf104381l.md
# 这里不能用dijstra 最短路的原因是每层的边cost不一致,所以用分层DP更快




import init_setting
from cflibs import *
from lib.UnionFind import *
def main():
    n, m, T = MII()
    T -= 1
    
    uf = UnionFind(n)
    edges = []
    
    for _ in range(m):
        u, v, x = MII()
        u -= 1
        v -= 1
        if x == 0: uf.merge(u, v)
        else: edges.append((u, v, x))
    
    dp = [[inf] * n for _ in range(n)]
    dp[0][uf.find(0)] = 0
    
    ans = inf
    
    for i in range(n - 1):
        for u, v, x in edges:
            u = uf.find(u)
            v = uf.find(v)
            dp[i + 1][v] = fmin(dp[i + 1][v], dp[i][u] + i * x)
            dp[i + 1][u] = fmin(dp[i + 1][u], dp[i][v] + i * x)
    
    for i in range(n):
        ans = fmin(ans, dp[i][uf.find(T)])
    
    print(ans if ans < inf else -1)