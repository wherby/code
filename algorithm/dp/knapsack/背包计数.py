# https://codeforces.com/gym/103940/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0226/solution/cf103940a.md
# 因为C比较小，所以可以用bellman-ford算法计算出每个点的最短路径，因为每次遍历会使得路径增加一，而上限是C，则C次遍历一定能找打最佳路径，
# 然后背包dp计算出方案数 注意dp数组的定义是dp[i]表示花费i的方案数，最后求和即可
# 背包计数，从小到到遍历值域就是完全背包，可以计算当前值的方案数
# 多重背包自动计算出了方案数


import init_setting
from lib.cflibs import *
def main(): 
    n, m, c = MII()
    mod = 10 ** 9 + 7
    
    needed = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v, w = MII()
        u -= 1
        v -= 1
        needed[v].append((u, w))
    
    dis = [c + 1] * n
    dis[0] = 1
    
    for _ in range(c):
        for u in range(1, n):
            res = 0
            for v, w in needed[u]:
                res += dis[v] + w
            dis[u] = fmin(dis[u], res)
    
    dp = [0] * (c + 1)
    dp[0] = 1
    
    for x in dis:
        for i in range(x, c + 1):
            dp[i] += dp[i - x]
            dp[i] %= mod
    
    print(sum(dp[1:]) % mod)