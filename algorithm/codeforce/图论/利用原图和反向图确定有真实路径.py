# https://codeforces.com/problemset/problem/164/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0903/solution/cf164a.md
# 在有向图中，如果只有原图路径标记，有可能路径没有达到汇点，只有反向图从汇点标记，路径在两者都有的点，才是在valid(从源到汇)的路径上

import init_setting
from cflibs import *
def main():
    n, m = MII()
    vals = LII()
    
    path = [[] for _ in range(n)]
    rev_path = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v = GMI()
        path[u].append(v)
        rev_path[v].append(u)
    
    vis1 = [0] * n
    que = []
    
    for i in range(n):
        if vals[i] == 1:
            vis1[i] = 1
            que.append(i)
    
    for u in que:
        for v in path[u]:
            if not vis1[v] and (vals[v] == 0 or vals[v] == 2):
                vis1[v] = 1
                que.append(v)
    
    vis2 = [0] * n
    que = []
    
    for i in range(n):
        if vals[i] == 2:
            vis2[i] = 1
            que.append(i)
    
    for u in que:
        if vals[u] == 1: continue
        
        for v in rev_path[u]:
            if not vis2[v]:
                vis2[v] = 1
                que.append(v)
    
    print('\n'.join(str(vis1[i] & vis2[i]) for i in range(n)))