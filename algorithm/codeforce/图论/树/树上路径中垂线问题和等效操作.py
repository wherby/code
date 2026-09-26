# https://codeforces.com/gym/106642/problem/I
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0815/solution/cf106642i.md
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0815/personal_submission/cf106642i_yawn_sean.py
# 这里做了基于数组更新的等效操作
# 这里对相等，大于，小于 距离需要做 z,x,y 的加法，这里先把相等的情况去除，在全局加上z,然后处理大于，小于的情况 x-z,y-z 这样就用两种操作等效代换了3种操作
# 对于大于或者小于的区间，其中一个区间一定是树的一颗完整的子树，对子树可以直接在数组中一次更新完成，对于不属于子树的情况更新：则先更新整颗树y, 再在去除子树部分更新-y消去
# 统一奇偶性划分：(d - 1) // 2 巧妙地一次性涵盖了奇数距离和偶数距离：
# 若 d 为奇数，例如 d = 3，(3 - 1) // 2 = 1，正好指向距离 u 为 1 的中边边界点；若d 为偶数，例如 d = 4，(4 - 1) // 2 = 1，正好指向距离 u 为 1（即中点靠近 u 侧的倒数第二个点）。
# 就是不论d 是奇数或者偶数：
#  这里（d-1)//2 是保证 查找到的点是U点出发的小于的区域
#  d - 1 - (d - 1) // 2 这里保证的是奇偶情况下，子树是大于等于的情况，但是这里处理的是子树的补集，也保证了补集区域是从U点出发的小于区域
#  然后用一个对称变换，使得大于，小于区域都能得到覆盖

import init_setting
from cflibs import *
from lib.lazySegmentTree import LazySegTree
# Submission link: https://codeforces.com/gym/106642/submission/387003977
def main():
    n, q = MII()
    path = [[] for _ in range(n)]
    
    for _ in range(n - 1):
        u, v = GMI()
        path[u].append(v)
        path[v].append(u)
    
    parent = [-1] * n
    depth = [0] * n
    stk = [0]
    
    ls = [0] * n
    rs = [0] * n
    
    tmstamp = 0
    
    while stk:
        u = stk.pop()
        if u >= 0:
            ls[u] = tmstamp
            tmstamp += 1
            stk.append(~u)
            for v in path[u]:
                if parent[u] != v:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    stk.append(v)
        else:
            rs[~u] = tmstamp
    
    nth_parent = [[-1] * n for _ in range(20)]
    nth_parent[0] = parent
    
    for i in range(19):
        for j in range(n):
            if nth_parent[i][j] != -1:
                nth_parent[i + 1][j] = nth_parent[i][nth_parent[i][j]]
    
    def merge(x, y):
        x1, x2 = divmod(x, n + 1)
        y1, y2 = divmod(y, n + 1)
        if x1 < y1: return x
        if x1 > y1: return y
        return x1 * (n + 1) + (x2 + y2)
    
    def mapping(x, y):
        return x * (n + 1) + y
    
    def composition(x, y):
        return x + y
    
    def lca(u, v):
        if depth[u] > depth[v]:
            u, v = v, u
        
        d = depth[v] - depth[u]
        while d:
            x = d & -d
            v = nth_parent[x.bit_length() - 1][v]
            d -= x
        
        if u == v:
            return u
    
        for i in range(19, -1, -1):
            if nth_parent[i][u] != nth_parent[i][v]:
                u = nth_parent[i][u]
                v = nth_parent[i][v]
        
        return parent[u]
    
    def kth_parent(k, u):
        for i in range(20):
            if k >> i & 1:
                u = nth_parent[i][u]
        return u
    
    seg = LazySegTree(merge, 10 ** 15 * (n + 1), mapping, composition, 0, [1] * n)
    total_lazy = 0
    
    outs = []
    
    for _ in range(q):
        u, v, x, y, z = MII()
        u -= 1
        v -= 1
        x -= z
        y -= z
        total_lazy += z
        
        if u != v:
            l = lca(u, v)
            d = depth[u] + depth[v] - depth[l] * 2
            
            for _ in range(2):
                if depth[u] - depth[l] > (d - 1) // 2:
                    pos = kth_parent((d - 1) // 2, u)
                    seg.apply(ls[pos], rs[pos], x)
                else:
                    pos = kth_parent(d - 1 - (d - 1) // 2, v)
                    total_lazy += x
                    seg.apply(ls[pos], rs[pos], -x)
                
                u, v = v, u
                x, y = y, x
        
        val, cnt = divmod(seg.all_prod(), n + 1)
        val += total_lazy
        
        outs.append(f'{val} {cnt}')
    
    print('\n'.join(outs))


main()