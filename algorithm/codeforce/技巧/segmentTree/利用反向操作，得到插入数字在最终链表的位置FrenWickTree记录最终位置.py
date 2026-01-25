# https://codeforces.com/gym/105617/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0123/solution/cf105617e.md
# 利用反向操作，得到插入数字在最终链表的位置
# 使用 FenwickTreeArray 寻找最终的位置，从后到前就是把位置置0

import init_setting
from cflibs import *
from lib.segmentTreeWithFuction import segment_tree
from lib.fenwicktree import FenwickTreeArray 
def main(): 
    n = II()
    nums = LII()
    
    fen = FenwickTreeArray([1] * n)
    pos = [0] * n
    
    for i in range(n - 1, -1, -1):
        pos[i] = fen.bisect_min_larger(nums[i])
        fen.add(pos[i], -1)
    
    max_fen = segment_tree([0]*n,max)
    ans = 0
    outs = []
    
    for i in range(n):
        res = max_fen.query(0,pos[i]) + 1
        ans = fmax(ans, res)
        outs.append(ans)
        max_fen.set(pos[i], res)
    
    print('\n'.join(map(str, outs)))

main()