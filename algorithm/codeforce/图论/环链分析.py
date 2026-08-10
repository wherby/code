# https://codeforces.com/gym/106159/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0806/solution/cf106159g.md
# 一个点两条边构成的图，最多是环，或者链
# 在环或链的子图中，不取相邻点，环和链的最多取值点是不一样的。所以需要检测当前连接是链还是环


import init_setting
from cflibs import *
from lib.UnionFind import *
def main():
    n = II()
    nums = LII()
    
    p = LGMI()
    path = [[] for _ in range(n)]
    
    for i in range(n):
        path[p[i]].append(i)
        path[i].append(p[i])
    
    ans = 0
    cur = 0
    
    uf = UnionFind(n)
    vis = [0] * n
    
    for i in sorted(range(n), key=lambda x: -nums[x]):
        vis[i] = 1
        cur += 1
        
        for j in path[i]:
            if vis[j]:
                if uf.find(i) != uf.find(j):
                    cur -= (uf.getSize(i) + 1) // 2
                    cur -= (uf.getSize(j) + 1) // 2
                    uf.merge(i, j)
                    cur += (uf.getSize(i) + 1) // 2
                else:
                    cur -= uf.getSize(i) % 2
        
        ans = fmax(ans, cur * nums[i])
    
    print(ans)