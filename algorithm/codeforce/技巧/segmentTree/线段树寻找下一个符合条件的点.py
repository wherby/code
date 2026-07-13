# https://codeforces.com/gym/103821/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0708/solution/cf103821a.md
# 利用线段树寻找下一个符合条件的点，这里用SortedList更简单


import init_setting
from cflibs import *
from lib.segTreeWithFindFirst import  SegTree
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n, q = MII()
        tmp = [[] for _ in range(n)]
        
        for i in range(q):
            x1, x2, y = MII()
            x1 -= 1
            x2 -= 1
            tmp[y].append((x1, x2))
        
        seg = SegTree(fmax, 0, [1] * n)
        
        for i in range(n):
            for l, r in tmp[i]:
                if seg.prod(l, r + 1):
                    while True:
                        p = seg.max_right(l, lambda x: x == 0)
                        if p <= r: seg.set(p, 0)
                        else: break
                    seg.set(l, 1)
                    seg.set(r, 1)
        
        outs.append(sum(seg.get(i) for i in range(n)))
    
    print('\n'.join(map(str, outs)))