# https://codeforces.com/gym/106687/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0909/solution/cf106687e.md
# algorithm/codeforce/docs/basic/在线重编码.md
# 可以使用类似前缀数组的BFS重排列编码方式，这里是用在线重编码的方式更直接，每次记录最短路的相对大小





import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    mod = 998244353
    
    for _ in range(t):
        n, m, k = MII()
        path = [[] for _ in range(n)]
        
        for _ in range(m):
            u, v, w = MII()
            u -= 1
            v -= 1
            path[u].append(w * n + v)
            path[v].append(w * n + u)
        
        def f(prev_dis, edge, u):
            return (prev_dis * k + edge) * n + u
        
        dis = [(n, k)] * n
        dis[0] = (0, 0)
        
        dis_idx = [n] * n
        dis_idx[0] = 0
    
        ans = [-1] * n
        ans[0] = 0
        
        pq = [f(0, 0, 0)]
        
        cur_prev_dis = 0
        cur_edge = 0
        cur_idx = 0
        
        while pq:
            msk = heappop(pq)
            
            msk, u = divmod(msk, n)
            prev_dis, edge = divmod(msk, k)
            
            if dis[u] == (prev_dis, edge):
                if (prev_dis, edge) > (cur_prev_dis, cur_edge):
                    cur_prev_dis = prev_dis
                    cur_edge = edge
                    cur_idx += 1
                dis_idx[u] = cur_idx
                
                for msk in path[u]:
                    d, v = divmod(msk, n)
                    if dis[v] > (dis_idx[u], d):
                        dis[v] = (dis_idx[u], d)
                        ans[v] = (ans[u] * k + d) % mod
                        heappush(pq, f(dis_idx[u], d, v))
        
        outs.append(' '.join(map(str, ans)))
    
    print('\n'.join(outs))