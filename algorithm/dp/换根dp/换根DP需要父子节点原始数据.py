# https://codeforces.com/gym/106507/problem/K
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/05/0521/solution/cf106507k.md
# 题目中求任意K个节点到根的路径和，正好对应每个节点下的组合数，因为如果K个节点都是当前节点子节点的时候，会在子节点上也计算一遍，这种重复包含关系正好对应了路径的权值
# 而在换根的时候，需要计算换根的时候产生的DIFF， u-v换根的时候，sz[v]对应的组合都要少一，而n-sz[v]对应的组合都要加1， 
# algorithm/codeforce/dp/docs/换根DP的贡献计算法.md 这里采用了贡献法，虽然看起来更复杂，但是在其他题目可能更好，因为这种贡献法可能会更好处理非线性的值
# (dp[u] - dp[v] - f.combi(sz[v], k))  这里是转移的时候，U节点除去了v子树的贡献，并且由于v节点变根节点的时候，组合减少的数量
# rev_dp[u]  表示U 节点外数的贡献
#  f.combi(n - sz[v], k) 表示的是 v节点变更节点之后，其他组合增加的数量

import init_setting
from lib.cflibs import *
from lib.combineWithPreCompute import *
def main():  
    n, k = MII()
    path = [[] for _ in range(n)]
    
    for _ in range(n - 1):
        u, v = GMI()
        path[u].append(v)
        path[v].append(u)
    
    mod = 10 ** 9 + 7
    f = Factorial(n, mod)
    
    parent = [-1] * n
    que = [0]
    
    for u in que:
        for v in path[u]:
            if parent[u] != v:
                parent[v] = u
                que.append(v)
    
    sz = [1] * n
    dp = [0] * n
    
    for u in reversed(que):
        if u:
            p = parent[u]
            sz[p] += sz[u]
            dp[p] += dp[u] + f.combi(sz[u], k)
            dp[p] %= mod
    
    rev_dp = [0] * n
    
    for u in que:
        for v in path[u]:
            if parent[v] == u:
                cur = (dp[u] - dp[v] - f.combi(sz[v], k)) % mod
                rev_dp[v] = (rev_dp[u] + cur + f.combi(n - sz[v], k)) % mod
    
    print(' '.join(str((dp[i] + rev_dp[i]) % mod) for i in range(n)))

main()