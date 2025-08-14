# https://codeforces.com/problemset/problem/1252/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0809/solution/cf1252b.md
# 树上路径数量DP，
# v1 表示 当前点作为路径内部点的情况
# v2 表示当前点作为路径端点的情况
# v3 表示当前点作为独立路径的情况， 所以只有一个点的时候值分别为 0,0,1
# 状态转移是在U端点在 把子节点 加入的情况下， 作为 v1,v2,v3 的情况，和子节点的dp0,dp1,dp2 进行合并计算
# dp0 表示 当前点事内部点的时候的时候， dp1，表示当前点为其中一个端点的时候， dp2表示当前点为独立路径的时候
# dp0 =v1 = (v1 * dp2[v] + v2 * dp1[v]) % mod 表示 当前节点如果是中间节点,中间节点对应其他不与它连接的节点是可以分割的，所以 v1 * dp2[v]，如果V2表示 U已经是一条路径的端点，如果V2的情况下与子节点连接，则当前节点又满足了是路径内点的条件 v2 * dp1[v]
# dp1 = (v2 +s2) = (v2*dp2[v] + v3*dp1[v]) +s2 * dp0[v]  
#       其中V2表示当前点作为路径端点 和子节点独立路径不冲突 ：v2*dp2[v] ， U 端点如果作为独立路径和子节点的路径端点合并，则U端点又变成了路径端点：  v3*dp1[v]
#       s2记录了当前独立路径的数量，与子节点为内部节点的情况独立：  s2 * dp0[v]   《=这里就是当前点为dp1状态下，其他没有被选中的点的状态数量
#       s1记录了当前节点与一个子节点连接的状态
# dp2[u] 的转移：u 是独立路径.   U是独立路径，有可能它作为分割点，所以独立路径的数字就可以把S1也计算上，
#       dp2[u] = (dp0[u] + s1 + s2)
#        这部分是 dp2[u] 的最终计算。它结合了所有可能的情况，其中 u 和其子树形成了完全独立的路径，不与父节点连接。
#        dp0[u]: u 是一个内部节点，其子树内的所有路径都已处理。
#        s1: u 是一个独立路径，其一个端点与子节点 v 连接。
#        s2: u 是一个独立路径，其不连接任何子节点。

# algorithm/codeforce/dp/树上DP根叶子互相影响/pic/p1.png
# algorithm/codeforce/dp/树上DP根叶子互相影响/pic/p2.png
# 每个节点在合并它的子节点的时候偶会产生状态转移， 其中 s1,s2 表示其他子节点的状态和当前状态无关的
# 当前节点作为独立路径的v3可以和子节点dp1 合并成 新的 dp1 因为 dp1是新的一个端点
# 当前节点为路径内端点的v2可以和dp1 合并当前节点是路径内部节点
# dp2是子端点已经完成的路径的数字，和v1,v2,v3的状态都无关，
# s1 辅助记录当前节点是端点，s1：在处理子节点 v 之前，u 已经是一个独立路径的端点，并向下连接到了其他子节点。 dp[0]表示的是子节点已经是内部节点，所以他们没有连接  s1 * dp0[v]
#                        s2: 在处理子节点v之的独立的路径，dp1[v] 表示子节点v是单独节点，既然v是单独节点，就可以和当前节点合并，成为新的单独节点的数字       s2 * dp1[v]                   
# 
# 对于每次合并的时候， v1,v2,v3是合并之后的状态，由合并之前的状态转移过来，s1表示当前节点是【active状态：可以和它的上级节点合并] 的个数， 和s2当前独立路径的个数累计，dp0[u]表示当前点是内部节点，是由于u作为内部节点的时候才完成独立路径的个数

import init_setting
from lib.cflibs import *
def main():
    n = II()
    mod = 10 ** 9 + 7
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
    
    dp0 = [0] * n
    dp1 = [0] * n
    dp2 = [0] * n
    
    for u in reversed(que):
        v1, v2, v3 = 0, 0, 1
        s1, s2 = 0, 1
        
        for v in path[u]:
            if parent[v] == u:
                v1 = (v1 * dp2[v] + v2 * dp1[v]) % mod
                v2 = (v2 * dp2[v] + v3 * dp1[v]) % mod
                v3 = v3 * dp2[v] % mod
                
                s1 = (s1 * dp0[v] + s2 * dp1[v]) % mod
                s2 = s2 * dp0[v] % mod
        
        dp0[u] = v1
        dp1[u] = (v2 + s2) % mod
        dp2[u] = (dp0[u] + s1 + s2) % mod
    
    print(dp2[0])