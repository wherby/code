# https://codeforces.com/gym/101879/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1010/solution/cf101879c.md
# 这里处理的是，需要构造一个与已知图的节点一样奇偶性的图
# 由于K个连线的图可能是多个联通图，
# 而联通图中点的奇偶性在生成树上调节，通过反向贪心使用差分的方式传递奇偶性和，得到最优解，然后测试最优解是不是正确解
# algorithm/codeforce/图论/docs/联通图的节点奇偶性传递.md


import init_setting
from cflibs import *
from lib.UnionFind import UnionFind
def main():
    n, m, k = MII()
    
    degs = [0] * n
    
    for _ in range(m):
        u, v = GMI()
        degs[u] ^= 1
        degs[v] ^= 1
    
    uf = UnionFind(n)
    path = [[] for _ in range(n)]
    
    for _ in range(k):
        u, v = GMI()
        if uf.merge(u, v):
            path[u].append(v)
            path[v].append(u)
    
    parent = [-1] * n
    
    que = [i for i in range(n) if uf.find(i) == i]
            
    for u in que:
        for v in path[u]:
            if parent[u] != v:
                parent[v] = u
                que.append(v)
    
    for u in reversed(que):
        if parent[u] != -1:
            degs[parent[u]] ^= degs[u]
    
    for i in range(n):
        if parent[i] == -1 and degs[i]:
            exit(print('NO'))
    
    print('YES')
    k = sum(degs)
    print(k)
    if k: print('\n'.join(f'{i + 1} {parent[i] + 1}' for i in range(n) if degs[i]))