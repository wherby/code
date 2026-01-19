# https://codeforces.com/gym/105317/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0113/solution/cf105317e.md
# 树上路径的值使用LCA 查询
# 对每个点值的平方数处理，使用Prime的递推技巧
# 最后对L有限制，所以就需要对prime 组合进行DP，这里DP需要有两个状态，已经选择的次数和，当前的余数，最开始的状态0  dp[0] =1 ,remaining[0] =1 是为了DP状态转移，最后需要把Dp[0] = 0 为了计算



import init_setting
from cflibs import *
def main(): 
    M = 70
    pr = list(range(M + 1))
    primes = []
    
    for i in range(2, M + 1):
        if pr[i] == i:
            primes.append(i)
            for j in range(i, M + 1, i):
                pr[j] = i
    
    msks = [0] * (M + 1)
    for i in range(19):
        msks[primes[i]] = 1 << i
    
    for i in range(2, M + 1):
        if pr[i] < i:
            msks[i] = msks[i // pr[i]] ^ msks[pr[i]]
    
    n, l = MII()
    
    k = len(primes)
    dp = [100] * (1 << k)
    remaining = [1] * (1 << k)
    
    dp[0] = 1
    for i in range(1 << k):
        for j in range(k):
            if i >> j & 1: continue
            ni = i | (1 << j)
            
            x = dp[i]
            y = remaining[i]
            if y * primes[j] <= l:
                y *= primes[j]
            else:
                x += 1
                y = primes[j]
            
            if x < dp[ni] or (x == dp[ni] and y < remaining[ni]):
                dp[ni] = x
                remaining[ni] = y
    dp[0] = 0
    
    nums = LII()
    for i in range(n):
        nums[i] = msks[nums[i]]
    
    path = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = GMI()
        path[u].append(v)
        path[v].append(u)
    
    depth = [0] * n
    parent = [-1] * n
    que = [0]
    
    for u in que:
        for v in path[u]:
            if parent[u] != v:
                parent[v] = u
                depth[v] = depth[u] + 1
                nums[v] ^= nums[u]
                que.append(v)
    
    nth_parent = [[-1] * n for _ in range(20)]
    nth_parent[0] = parent
    
    for i in range(19):
        for j in range(n):
            if nth_parent[i][j] >= 0:
                nth_parent[i + 1][j] = nth_parent[i][nth_parent[i][j]]
    
    def lca(x, y):
        if depth[x] > depth[y]:
            x, y = y, x
        
        d = depth[y] - depth[x]
        while d:
            v = d & -d
            y = nth_parent[v.bit_length() - 1][y]
            d -= v
        
        if x == y: return x
        
        for i in range(19, -1, -1):
            if nth_parent[i][x] != nth_parent[i][y]:
                x = nth_parent[i][x]
                y = nth_parent[i][y]
        
        return parent[x]
    
    q = II()
    outs = []
    
    for _ in range(q):
        u, v = GMI()
        l = lca(u, v)
        
        val = nums[u] ^ nums[v] ^ nums[l]
        if l > 0: val ^= nums[parent[l]]
    
        outs.append(dp[val])
    
    print('\n'.join(map(str, outs)))