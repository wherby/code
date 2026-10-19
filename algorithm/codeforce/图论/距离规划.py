# https://codeforces.com/gym/106760/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1013/solution/cf106760d.md
# 解答是需要在原图中任意有公共点的两个点都添加路径，由于原图本来就有可能有路径，所以直接用dp记录最终所有的路径


import init_setting
from lib.cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n, m = MII()
        path = [[] for _ in range(n)]
        
        for _ in range(m):
            u, v = GMI()
            path[u].append(v)
            path[v].append(u)
        
        vis = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in path[i]:
                vis[i][j] = 1
            for j1 in path[i]:
                for j2 in path[i]:
                    vis[j1][j2] = 1
        
        out = []
        for i in range(n):
            for j in range(i + 1, n):
                if vis[i][j]:
                    out.append(f'{i + 1} {j + 1}')
        
        outs.append(f'{len(out)}')
        outs.extend(out)
    
    print('\n'.join(outs))