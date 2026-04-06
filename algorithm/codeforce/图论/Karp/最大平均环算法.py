# https://codeforces.com/gym/106443/problem/I
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0401/solution/cf106443i.md
# algorithm/graph/Karp/Karp最小最大平均环算法.md
# 在计算dis 的时候，取了max值，所以可以保证如果在大环的点

import init_setting
from cflibs import *

def main(): 
    n, m = MII()
    path = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v, w = MII()
        u -= 1
        v -= 1
        path[u].append(w * n + v)
    
    inf = 10 ** 15
    dis = [[-inf] * n for _ in range(n + 1)]
    
    dis[0][0] = 0
    
    for i in range(n):
        for u in range(n):
            if dis[i][u] != -inf:
                for msk in path[u]:
                    w, v = divmod(msk, n)
                    dis[i + 1][v] = fmax(dis[i + 1][v], dis[i][u] + w)
    
    ans = 0
    for u in range(n):
        if dis[n][u] != -inf:
            tmp = inf
            for i in range(n):
                if dis[i][u] != -inf:
                    tmp = fmin(tmp, (dis[n][u] - dis[i][u]) / (n - i))
            ans = fmax(ans, tmp)
    
    print(ans)

if __name__ == '__main__':
    main()