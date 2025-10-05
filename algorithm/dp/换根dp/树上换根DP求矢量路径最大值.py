# https://codeforces.com/gym/105012/problem/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1003/solution/cf105012j.md
# 这里求的是矢量路径，函数值在就是起点和终点是有方向的
# 先计算逆DFS序，这样计算的DFS值是从叶子到根的方向，
# 然后用正DFS序遍历，得到从根到叶子方向的换根DP，对叶子的DP因为记录了最大值和次大值，就用当前路径寻找与当前路径不重合的最大值进行DP


import init_setting
from cflibs import *
def main():
    n = II()
    nums = LII()
    
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
    
    def f(x, y):
        return fmax(x, y) + math.isqrt(fmin(x, y))
    
    que.reverse()
    
    dp1 = [0] * n
    dp2 = [0] * n
    
    for u in que:
        dp1[u] = nums[u]
        
        for v in path[u]:
            if parent[v] == u:
                dp1[u] = fmax(dp1[u], f(dp1[v], nums[u]))
    
    que.reverse()
    
    for u in que:
        dp2[u] = fmax(dp2[u], nums[u])
        v1, v2 = dp2[u], 0
        
        for v in path[u]:
            if parent[v] == u:
                nv = f(dp1[v], nums[u])
                if nv > v1: v1, v2 = nv, v1
                elif nv > v2: v2 = nv
        
        for v in path[u]:
            if parent[v] == u:
                nv = f(dp1[v], nums[u])
                if nv == v1: dp2[v] = f(v2, nums[v])
                else: dp2[v] = f(v1, nums[v])
    
    print(fmax(max(dp1), max(dp2)))