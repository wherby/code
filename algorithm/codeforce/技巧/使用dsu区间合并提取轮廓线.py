# https://codeforces.com/problemset/problem/35/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0710/solution/cf35e.md
# 使用区间合并DSU 从大到小，每次合并都是外轮廓线
# 利用每个点的高度变化，画出轮廓线

import init_setting
from cflibs import *
def main():
    delta = random.getrandbits(30)

    infile = open('input.txt', 'r')
    input = lambda: infile.readline().strip()
    outfile = open('output.txt', 'w')
    print = lambda x: outfile.write(str(x) + '\n')

    n = II()

    ls = []
    rs = []
    hs = []

    for _ in range(n):
        h, l, r = MII()
        l += delta
        r += delta
        ls.append(l)
        rs.append(r)
        hs.append(h)

    seps = sorted(set(ls + rs))
    k = len(seps)
    d = {v: i for i, v in enumerate(seps)}

    vals = [0] * k
    dsu = UnionFind(k)

    for i in sorted(range(n), key=lambda x: -hs[x]):
        pl = d[ls[i]]
        pr = d[rs[i]]
        h = hs[i]
        while dsu.find(pl) < pr:
            pl = dsu.find(pl)
            vals[pl] = h
            dsu.merge_to(pl, pl + 1)

    pts = []
    cur_h = 0

    for i in range(k):
        if vals[i] != cur_h:
            pts.append(f'{seps[i] - delta} {cur_h}')
            pts.append(f'{seps[i] - delta} {vals[i]}')
            cur_h = vals[i]

    print(len(pts))
    print('\n'.join(pts))