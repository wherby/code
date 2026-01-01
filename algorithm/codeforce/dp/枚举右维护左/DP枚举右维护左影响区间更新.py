# https://codeforces.com/gym/106290/problem/H
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/01/0101/solution/cf106290h.md
# 枚举右维护左，在SegmentTree 里维护当前节点为右节点的时候，左节点在哪里才能获得当前值的额外1 
# 如果当前值不是该值的最右的值，则从0 到当前值都可以增加1， 而影响是从上一个值开始的区间到当前值的区间都需要增加1，
# 如果当值值是该值的最右值，则从0开始到当前值的区间不正确了，应该取消，变成第一个当前值后一个区间到当前值的区间是有效的
# seg.apply(first_pos[nums[i]] + 1, last_pos[nums[i]] + 1, 1) 如果当前值是最右值的时候，last_pos[nums[i]] + 1 理论可以是n， 但是对于枚举右维护左的时候，最大值就是last_pos[nums[i]] + 1

import init_setting
from cflibs import *
from lib.lazySegmentTree import LazySegmentTree
def main(): 
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        nums = LII()
        
        first_pos = [-1] * (n + 1)
        last_pos = [-1] * (n + 1)
        prev = [0] * n
        
        for i in range(n):
            prev[i] = last_pos[nums[i]]
            last_pos[nums[i]] = i
            if first_pos[nums[i]] == -1:
                first_pos[nums[i]] = i
        
        ans = 0
        seg = LazySegmentTree(n,fmax, 0, add, add, 0)
        
        for i in range(n + 1):
            if last_pos[i] != -1:
                ans += 1
        
        to_add = 0
        
        for i in range(n):
            if last_pos[nums[i]] != i:
                seg.apply(prev[i] + 1, i + 1, 1)
            elif prev[i] != -1:
                seg.apply(0, prev[i] + 1, -1)
                seg.apply(first_pos[nums[i]] + 1, last_pos[nums[i]] + 1, 1)
            to_add = fmax(to_add, seg.all_prod())
        
        outs.append(ans + to_add)
    
    print('\n'.join(map(str, outs)))

main()