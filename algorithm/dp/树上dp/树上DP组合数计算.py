# https://codeforces.com/gym/106463/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0407/solution/cf106463b.md
# 因为组合数是与子树的个数奇偶性相关，所以用逆DFS序处理
# 计数变量：c0 与 c1
# c0 (Count Even)：大小为偶数的子树个数。
# c1 (Count Odd)：大小为奇数的子树个数。
# algorithm/codeforce/dp/docs/奇偶分布子树的色彩组合数的计算.md 
# 奇数子树分配：$\binom{c1}{\lfloor c1/2 \rfloor}$ 种方案分配子树根节点的颜色。
# 偶数子树自由度：如果存在奇数子树（c1 > 0），每个偶数子树都有 $2$ 种放置位置（奇数个奇数子树之后或偶数个之后），导致 $2^{c0}$ 种方案。


import init_setting
from lib.cflibs import *
from lib.combineWithPreCompute import Factorial
def main(): 
    t = II()
    outs = []
    
    M = 10 ** 5
    mod = 10 ** 9 + 7
    f = Factorial(M, mod)
    
    for _ in range(t):
        n = II()
        path = [[] for _ in range(n)]
        
        for _ in range(n - 1):
            u, v = GMI()
            path[u].append(v)
            path[v].append(u)
        
        que = [0]
        parent = [-1] * n
        
        for u in que:
            for v in path[u]:
                if parent[u] != v:
                    parent[v] = u
                    que.append(v)
        
        dp = [1] * n
        sz = [1] * n
        
        for u in reversed(que):
            c0 = 0
            c1 = 0
            
            for v in path[u]:
                if parent[v] == u:
                    if sz[v]:
                        sz[u] ^= 1
                        c1 += 1
                    else:
                        c0 += 1
                    dp[u] = dp[u] * dp[v] % mod
    
            dp[u] = dp[u] * f.combi(c1, c1 // 2) % mod
            if c1: dp[u] = dp[u] * pow(2, c0) % mod
        
        outs.append(dp[0])
    
    print('\n'.join(map(str, outs)))

main()