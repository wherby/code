# https://codeforces.com/gym/104848/problem/M
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1018/solution/cf104848m.md
# Fi=vi *ci     li/ci = ti 
# ti = li /(Fi/ci) = li*ci /Fi 
# Sum( li*ci /Fi ) = T
# 因为(a1**2 + a2**2 + .. + an**2) *(b1**2 + b2 **2 + ..+ bn**2) >= (a1*b1 + a2*b2 +..+an*bn)
# 这时  T* sum(Fi) >= sum(sqrt(li*ci))
# 所以每一段的cost最小值 是 1/T  *sqrt(li*ci))
# /Users/tao/software/code/algorithm/codeforce/数论/数学/不等式转换/p1.png
# /Users/tao/software/code/algorithm/codeforce/数论/数学/不等式转换/p2.png

import init_setting
from cflibs import *
def main(): 
    n, m, T = MII()
    path = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v, l, c = MII()
        u -= 1
        v -= 1
        w = math.sqrt(l * c)
        
        path[u].append((v, w))
        path[v].append((u, w))
    
    pq = [(0, 0)]
    
    dis = [10 ** 15] * n
    dis[0] = 0
    
    while pq:
        d, u = heappop(pq)
        
        if dis[u] == d:
            for v, w in path[u]:
                nd = d + w
                if nd < dis[v]:
                    dis[v] = nd
                    heappush(pq, (dis[v], v))
    
    print(dis[-1] * dis[-1] / T)