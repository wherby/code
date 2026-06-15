
# https://codeforces.com/gym/105757/problem/N
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0611/solution/cf105757n.md

# algorithm/codeforce/docs/树上点集的路径判定算法.md
# 树上路径判定方式，从每个点往上找，如果可以找到2条以上的分叉，则不是简单路径
# 一个连通的树节点集合 $S$ 能排成一条“简单路径”，当且仅当 $S$ 的导出子图中，所有点的度数（Degree）最大值 $\le 2$。
# 当K>2时候，则最多只有星型连接，中间是0，才能有1的MEX


import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        path = [[] for _ in range(n)]
        
        for _ in range(n - 1):
            u, v = MII()
            path[u].append(v)
            path[v].append(u)
        
        parent = [-1] * n
        que = [0]
        
        for u in que:
            for v in path[u]:
                if parent[u] != v:
                    parent[v] = u
                    que.append(v)
        
        vis = [0] * n
        vis[0] = 1
        
        degs = [0] * n
        ans = 0
        flg = True
        
        for i in range(1, n):
            cur = i
            while not vis[cur]:
                vis[cur] = 1
                degs[cur] += 1
                degs[parent[cur]] += 1
                cur = parent[cur]
                if degs[cur] > 2:
                    flg = False
            if flg: ans = i
        
        out = [0] * (n - 1)
        out[0] = ans + 1
        
        for i in range(1, len(path[0])):
            out[i] = 1
        
        outs.append(' '.join(map(str, out)))
    
    print('\n'.join(outs))