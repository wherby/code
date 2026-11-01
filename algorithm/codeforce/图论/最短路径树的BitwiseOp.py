# https://codeforces.com/gym/106795/problem/H
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1030/solution/cf106795h.md
# 这里用bitwise 记录每个目的点，然后用反BFS序，回归记录路径点是否在最近路径上
# 


import init_setting
from cflibs import *
def main(): 
    n, m, k = MII()
    nodes = LGMI()
    
    path = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v = GMI()
        path[u].append(v)
        path[v].append(u)
    
    dis = [-1] * n
    dis[0] = 0
    
    que = [0]
    
    for u in que:
        for v in path[u]:
            if dis[v] == -1:
                dis[v] = dis[u] + 1
                que.append(v)
    
    bs = [0] * n
    
    for i in range(k):
        bs[nodes[i]] = 1 << i
    
    for i in reversed(que):
        for j in path[i]:
            if dis[j] == dis[i] + 1:
                bs[i] |= bs[j]
    
    print(max(dis[i] for i in range(n) if bs[i] == bs[0]))