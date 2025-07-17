# https://codeforces.com/problemset/problem/1833/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0705/solution/cf1833e.md

import init_setting
from cflibs import *
def main():
    t = II()
    outs = []

    for _ in range(t):
        n = II()
        nums = LGMI()
        dsu = UnionFind(n)
        
        deg = [0] * n
        total = n
        vis = set()
        
        for i in range(n):
            u, v = i, nums[i]
            if u > v: u, v = v, u
            
            if (u, v) not in vis:
                deg[u] += 1
                deg[v] += 1
            vis.add((u, v))
            
            if dsu.merge(v, u):
                total -= 1
        
        cnt = deg.count(1)
        outs.append(f'{fmin(total, total + 1 - cnt // 2)} {total}')

    print('\n'.join(outs))