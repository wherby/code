# https://codeforces.com/gym/103316/problem/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0304/solution/cf103316j.md
# 使用DSU求解图形合并时的最大值最小值的贡献
# 使用贡献法求解路径的最大值最小值差的和
# 也是证明了完整图分割的时候cost函数是x*y的形式，这时的所有cost和是C(N,2)



import init_setting
from cflibs import *
from lib.UnionFind import UnionFind
def main(): 
    n = II()
    nums = LII()
    
    path = [[] for _ in range(n)]
    
    for _ in range(n - 1):
        u, v = GMI()
        path[u].append(v)
        path[v].append(u)
    
    st_range = sorted(range(n), key=lambda x: nums[x])
    
    ans = 0
    mod = 10 ** 9 + 7
    
    vis = [0] * n
    uf = UnionFind(n)
    
    for u in st_range:
        for v in path[u]:
            if vis[v]:
                ans = (ans + nums[u] * uf.getSize(u) % mod * uf.getSize(v) % mod) % mod
                uf.merge(u, v)
        vis[u] = 1
    
    for i in range(n): vis[i] = 0
    uf.init()
    
    for u in reversed(st_range):
        for v in path[u]:
            if vis[v]:
                ans = (ans + mod - nums[u] * uf.getSize(u) % mod * uf.getSize(v) % mod) % mod
                uf.merge(u, v)
        vis[u] = 1
    
    print(ans * pow(n * (n - 1) // 2 % mod, -1, mod) % mod)

if __name__ == '__main__':
    main()