# https://codeforces.com/gym/105863/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/12/1211/solution/cf105863f.md
# 有效的模运算隐含的性质是 余数是比原数 小一半以上，所以任何数字的有效模运算最多只有 log2 个


import init_setting
from cflibs import *
from lib.segTreeWithFindFirst import SegmentTree as SegTree
def main(): 
    t = II()
    outs = []
    inf = 2 * 10 ** 9
    
    for _ in range(t):
        n, q = MII()
        nums = LII()
        
        seg = SegTree( fmin, inf,nums)
        for _ in range(q):
            x = II()
            
            pt = 0
            while x:
                pt = seg.max_right(pt, lambda val: val > x)+1
                if pt == n: break
                x = x % nums[pt]
                print(x,nums[pt],pt)
            
            outs.append(x)
    
    print('\n'.join(map(str, outs)))

main()