# http://codeforces.com/gym/104158/problem/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0227/solution/cf104158j.md
# 因为题目求的是相邻高度差，所以区间增加只有前后会变化，正好对应了差分标记值



import init_setting
from cflibs import *
from lib.segTreeWithFindFirst import  SegTree
def main(): 
    n, q, k = MII()
    
    nums = LII()
    nums.sort()
    
    seg = SegTree(fmax, 0, k + 5)
    outs = []
    
    for _ in range(q):
        l, r, x = MII()
        l -= 1
        if l: seg.set(l, seg.get(l) + x)
        seg.set(r, seg.get(r) - x)
        outs.append(n - bisect.bisect_left(nums, seg.all_prod()))
    
    print('\n'.join(map(str, outs)))
main()