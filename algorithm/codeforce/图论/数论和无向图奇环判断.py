# https://codeforces.com/gym/105059/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/05/0529/solution/cf105059c.md
# 除了2的质数都是奇数，无向图一定能构成该奇数的倍数
# 如果是2的时候，就需要验证路径是否是奇数且没有奇数环

import init_setting
from cflibs import *
def main():
    n, m, g = MII()
    
    if g > 2: print(0)
    else:
        path = [[] for _ in range(n)]
        
        for _ in range(m):
            u, v = GMI()
            path[u].append(v)
            path[v].append(u)
        
        dis = [-1] * n
        
        que = [0]
        dis[0] = 0
        
        flg = True
        
        for u in que:
            for v in path[u]:
                if dis[v] == -1:
                    dis[v] = dis[u] ^ 1
                    que.append(v)
                elif dis[u] == dis[v]:
                    flg = False
        
        print(1 if flg and dis[-1] else 0)