# https://codeforces.com/gym/106527/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/05/0520/solution/cf106527d.md
# 有向图检测图上是否有环，图上最长路径长度小于67
# 用DP来标记图上当前点的最长路径，就可以不用当心长短支路的问题

import init_setting
from cflibs import *
def main():  
    n, m = MII()
    s = I()
    
    path = [[] for _ in range(n)]
    indeg = [0] * n
    
    for _ in range(m):
        u, v = GMI()
        path[u].append(v)
        indeg[v] += 1
    
    dp = [0] * n
    stk = [i for i in range(n) if indeg[i] == 0]
    
    while stk:
        u = stk.pop()
        
        for v in path[u]:
            dp[v] = fmax(dp[v], dp[u] + 1)
            indeg[v] -= 1
            if indeg[v] == 0:
                stk.append(v)
    
    if max(indeg) or max(dp) >= 67: print('NO')
    else:
        print('YES')
        print('\n'.join(s[0] for _ in range(m)))