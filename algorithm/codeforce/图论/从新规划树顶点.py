
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1119/solution/cf106007e.md
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1119/solution/cf106007e.md
# 因为要标记黑色路径，所以需要把两个点见的路径上的点变灰 ， 图原来有黑色节点，标记的时候也是在路径上标记，路径有标记可以使得标记复杂度为N
# 在新的图上，所有标记操作都是从叶子节点往根节点标记，

import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n, q = MII()
        s = [int(c) for c in I()]
        
        path = [[] for _ in range(n)]
        for _ in range(n - 1):
            u, v = GMI()
            path[u].append(v)
            path[v].append(u)
        
        queries = [II() - 1 for _ in range(q)]
        
        rt = queries[0]
        parent = [-1] * n
        
        que = [rt]
        
        for u in que:
            for v in path[u]:
                if parent[u] != v:
                    parent[v] = u
                    que.append(v)
        
        cols = [0] * n
        cnt = n
        
        for i in range(n):
            if s[i] == 0:
                u = i
                while u >= 0 and cols[u] == 0:
                    cols[u] = 1
                    cnt -= 1
                    u = parent[u]
        
        total = sum(s)
        
        for u in queries:
            if s[u]:
                s[u] = 0
                total -= 1
            
            while u >= 0 and cols[u] == 0:
                cols[u] = 1
                cnt -= 1
                u = parent[u]
            
            outs.append(cnt * (cnt + 1) // 2 + cnt * (total - cnt))
    
    print('\n'.join(map(str, outs)))