# https://codeforces.com/gym/101047/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1005/solution/cf101047d.md
# 因为跳转是均匀分布
# E(V) = E(不跳转) + E(跳转)    E（跳转） =  k+ E(V)
# (cur + k*(n-i) +(n-i)*V) = n*V    =》 V =（cur+ k*(n-i))/i 
# 但是这里 R = V + k = (cur+k*n)/i  R 表示先跳转之后的期望概率
# 对于0 这个点，选择需要考虑是否先跳转 还是直接不跳转，所以需要先求出R 

import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n, m, k = MII()
        path = [[] for _ in range(n)]
        
        for _ in range(m):
            u, v, w = MII()
            u -= 1
            v -= 1
            path[u].append(w * n + v)
            path[v].append(w * n + u)
        
        dis = [inf] * n
        dis[n - 1] = 0
        
        pq = [n - 1]
        
        while pq:
            d, u = divmod(heappop(pq), n)
            if dis[u] == d:
                for msk in path[u]:
                    w, v = divmod(msk, n)
                    if dis[v] > dis[u] + w:
                        dis[v] = dis[u] + w
                        heappush(pq, dis[v] * n + v)
        
        tmp = sorted(dis)
        
        ans = n * k
        cur = 0
        
        for i in range(1, n):
            cur += tmp[i - 1]
            res = (cur + k * n) / i
            if res <= tmp[i]:
                ans = fmin(ans, res)
        
        ans = fmin(ans, dis[0])
        outs.append(f'{ans:.10f}')
    
    print('\n'.join(outs))