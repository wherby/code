# https://codeforces.com/gym/106367/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0217/solution/cf106367g.md
# 线段树 + 二分查找
# 使用线段树查找满足条件的第一个位置，更新后继续查找，直到超出范围，
# 注意 线段树函数的定义，这里min_right, 在解法里用的是 max_right,lib 定义和题解的定义是相反的，注意使用lib的函数定义



import init_setting
from cflibs import *
from lib.segTreeWithFindFirst import SegmentTree as SegTree
def main(): 
    n, q = MII()
    nums = LII()
    seg = SegTree(fmax, -1, nums)
    
    outs = []
    for _ in range(q):
        l, r, val = MII()
        l -= 1
        
        ans = 0
        
        while True:
            # 寻找从 l 开始，第一个 >= val 的位置
            # min_right 会返回第一个使 check_func 为 True 的索引
            target_idx = seg.min_right(l, lambda x: x >= val)
            
            # 如果没找到，或者超出了查询范围 [l, r)
            # 注意：r 是 1-indexed 且通常是不包含的，这里 r 正好对应 0-indexed 的上限
            if target_idx == -1 or target_idx >= r:
                break
            
            # 从线段树中取值（因为原数组 nums 没更新）
            ans += seg.get(target_idx)
            
            # 魔法：提取后置为 -1（或比所有可能 val 都小的值）
            seg.set(target_idx, -1)
            
            # 下一次搜索从 target_idx + 1 开始，避免死循环
            l = target_idx + 1
            if l >= r:
                break
        
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))

main()