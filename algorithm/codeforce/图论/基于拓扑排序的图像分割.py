# https://codeforces.com/gym/106197/problem/H
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0915/solution/cf106197h.md
# 基于拓扑排序的图像分割
# 分割为可达区域，这里需要从目的地反推，因为可达性判定的时候，只有维护目的地的可达性区域才能利用题目条件。



import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n, m = MII()
        rev_path = [[] for _ in range(n)]
        out_deg = [0] * n
    
        for _ in range(m):
            u, v = GMI()
            rev_path[v].append(u)
            out_deg[u] += 1
        
        vis = [0] * n
        cur_deg = [0] * n
        
        vis[n - 1] = 1
        
        stk = [n - 1]
        
        while stk:
            u = stk.pop()
            
            for v in rev_path[u]:
                cur_deg[v] += 1
                
                if 2 * cur_deg[v] > out_deg[v] and not vis[v]:
                    vis[v] = 1
                    stk.append(v)
        
        if vis[0]: outs.append('-1')
        else:
            edges = []
            
            for u in range(n):
                for v in rev_path[u]:
                    if not vis[v] and vis[u]:
                        edges.append(f'{v + 1} {u + 1}')
            
            outs.append(f'{len(edges)}')
            
            for e in edges: outs.append(e)
    
    print('\n'.join(outs))