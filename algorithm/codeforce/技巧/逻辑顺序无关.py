# https://codeforces.com/problemset/problem/1210/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/06/0604/solution/cf1210a.md
# 这里最终求的是顺序数组的数量，所以和每个节点的数值是多少没有关系

import sys
sys.path.append("..")
from cflibs.cflibs import *
def main():
    n, m = MII()
    pairs = []

    for _ in range(m):
        u, v = GMI()
        pairs.append((u, v))

    if n <= 6: print(m)
    else:
        ans = 0
        for i in range(n):
            for j in range(i):
                vis = set()
                for u, v in pairs:
                    if u == i: u = j
                    if v == i: v = j
                    if u > v: u, v = v, u
                    vis.add((u, v))
                ans = fmax(ans, len(vis))
        
        print(ans)