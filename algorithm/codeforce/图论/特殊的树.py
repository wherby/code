# https://codeforces.com/problemset/problem/1238/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0822/solution/cf1238f.md
# 题目中给了区域连接的条件， 然后给了一棵树，并且给了连接的边，在树中选择subtree，使得连接的边也符合区域重叠必相连的条件
# 根据分析，a <-[L - [L1，R1]-[L2,R2]-....[LN ,RN]-R]-b 
# 每个点对应的线段的 只有在 L，R两个点能连接长链， 在中间只能连接一个点，否则就会有环，
# 换句话说就是每个点最多取两个长链 fmax(ans, x1 + x2 + 1 + (len(path[u]) - 2))
# 长链一边的点只能有一条长链。。 dp[u] = fmax(1, x1 + 1 + (sons_count - 1))

import init_setting
from cflibs import *
def main():
    t = II()
    inf = 10 ** 6
    outs = []
    
    for _ in range(t):
        n = II()
        path = [[] for _ in range(n)]
        
        for _ in range(n - 1):
            u, v = GMI()
            path[u].append(v)
            path[v].append(u)
        
        parent = [-1] * n
        que = [0]
        
        for u in que:
            for v in path[u]:
                if parent[u] != v:
                    parent[v] = u
                    que.append(v)
        
        ans = 0
        dp = [0] * n
        
        for u in reversed(que):
            x1, x2 = -inf, -inf
            for v in path[u]:
                if parent[v] == u:
                    if dp[v] > x1:
                        x1, x2 = dp[v], x1
                    elif dp[v] > x2:
                        x2 = dp[v]
            
            sons_count = len(path[u])
            if u > 0: sons_count -= 1
            
            dp[u] = fmax(1, x1 + 1 + (sons_count - 1))
            ans = fmax(ans, dp[u])
            ans = fmax(ans, x1 + x2 + 1 + (len(path[u]) - 2))
        
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))