# https://codeforces.com/gym/106039/problem/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/12/1208/solution/cf106035j.md


def describe(ll):
    print(ll.lst)
    print(ll.pre)
    print(ll.cur)

import init_setting
from cflibs import *
def main(): 
    n, m, s, t = MII()
    s -= 1
    t -= 1
    
    path = lst_lst(n)
    
    for _ in range(m):
        u, v = GMI()
        path.append(u, v)
        path.append(v, u)
    
    dis = [-1] * n
    que = [s]
    dis[s] = 0
    
    #describe(path)
    dist_nodes = lst_lst(n)
    
    for u in que:
        dist_nodes.append(dis[u], u)
        for v in path.iterate(u):
            if dis[v] == -1:
                dis[v] = dis[u] + 1
                que.append(v)
    #describe(dist_nodes)
    mod = 10 ** 9 + 7
    dp = [[0] * n for _ in range(2)]
    
    dp[0][s] = 1
    
    for i in range(n):
        for u in dist_nodes.iterate(i):
            for v in path.iterate(u):
                if dis[v] == dis[u]:
                    dp[1][v] += dp[0][u]
                    dp[1][v] %= mod
        
        for u in dist_nodes.iterate(i):
            for v in path.iterate(u):
                if dis[v] == dis[u] + 1:
                    dp[0][v] += dp[0][u]
                    dp[0][v] %= mod
                    dp[1][v] += dp[1][u]
                    dp[1][v] %= mod
    
    print(dp[1][t])

main()