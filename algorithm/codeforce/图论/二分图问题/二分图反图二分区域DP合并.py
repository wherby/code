# https://codeforces.com/gym/106125/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1025/solution/cf106125f.md
# 在完全图上做反图 上进行 二分图 划分
# 但是其中反图会出现多个二分区域包含不同的集合点
# 我们需要平均分配端点，可以使用DP 选择区域中的不同集合个数，使得端点数目相等 《=背包问题，反向寻找背包划分
# 




import init_setting
from cflibs import *
def main(): 
    n, m = MII()
    
    if n % 2 or n > 2005: exit(print('impossible'))
    
    path = [[1] * n for _ in range(n)]
    
    for _ in range(m):
        u, v = GMI()
        path[u][v] = path[v][u] = 0
    
    for i in range(n):
        path[i][i] = 0
    
    vis = [-1] * n
    groups = []
    cnts = []
    
    for i in range(n):
        if vis[i] == -1:
            vis[i] = 0
            que = [i]
            cnt = 0
            
            for u in que:
                for v in range(n):
                    if path[u][v]:
                        if vis[v] == -1:
                            vis[v] = 1 - vis[u]
                            cnt += vis[v]
                            que.append(v)
                        elif vis[u] == vis[v]:
                            exit(print('impossible'))
            
            groups.append(que)
            cnts.append(cnt)
    
    k = len(groups)
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    dp[0][0] = 1
    
    for i in range(k):
        c1 = cnts[i]
        c2 = len(groups[i]) - c1
        for j in range(n + 1):
            if dp[i][j]:
                dp[i + 1][j + c1] = 1
                dp[i + 1][j + c2] = 1
    
    if not dp[k][n // 2]:
        exit(print('impossible'))
    
    cur = n // 2
    chosen = []
    
    for i in range(k - 1, -1, -1):
        c1 = cnts[i]
        c2 = len(groups[i]) - c1
        if dp[i][cur - c1]: 
            chosen.append(c1)
            cur -= c1
        else:
            chosen.append(c2)
            cur -= c2
    
    chosen.reverse()
    
    for i in range(k):
        if chosen[i] != cnts[i]:
            for u in groups[i]:
                vis[u] ^= 1
    
    print('\n'.join('rb'[x] for x in vis))