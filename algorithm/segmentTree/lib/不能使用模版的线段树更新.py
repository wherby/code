# https://codeforces.com/gym/106494/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0423/solution/cf106494f.md
# 这里的查询和更新虽然是线段树操作，但是因为普通的线段树模版，设置的size一半是对齐操作，但是这个题目中每次分割的中点是和当前数组大小有关的，一半线段树模版则不是，所以不能直接套模版
# 而且在更新节点的时候，需要知道该节点对应的逻辑变化，所以需要用一个pos数组记录，而且在分左右节点的时候，使用了2倍关系，正好在push_up的时候可以使用这个关系
# 由于设置了default值的左右端点相等，所以在push_up的时候，处理左右不等的节点
# 因为数组不是幂对齐的长度，所以最后产生的节点数量会是 2.2 N 以下，所以这里开最大的2.2被最大长度
# 这里为了简单，处理M个节点，其实可以根据N的大小，设置处理区间


import init_setting
from cflibs import *
def main():
    n, q = MII()
    nums = LII()
    
    mod = 998244353
    rev2 = (mod + 1) // 2
    
    M = 2200000
    seg_tree = [0] * M
    dp = [1] * M
    
    ls = [-1] * M
    rs = [-1] * M
    pos = [0] * n
    
    ls[1] = 0
    rs[1] = n - 1
    
    for i in range(1, M):
        if rs[i] > ls[i]:
            mid = (ls[i] + rs[i]) // 2
            ls[2 * i] = ls[i]
            rs[2 * i] = mid
            ls[2 * i + 1] = mid + 1
            rs[2 * i + 1] = rs[i]
        elif ls[i] >= 0:
            pos[ls[i]] = i
    
    for i in range(M - 1, -1, -1):
        if ls[i] < rs[i]:
            mid = (ls[i] + rs[i]) // 2
            seg_tree[i] = seg_tree[2 * i] + seg_tree[2 * i + 1] + (nums[mid] > nums[mid + 1])
            if seg_tree[i] == 0: dp[i] = rs[i] - ls[i] + 1
            else: dp[i] = (dp[2 * i] + dp[2 * i + 1]) * rev2 % mod
    
    outs = []
    for _ in range(q):
        idx, val = MII()
        idx -= 1
        
        nums[idx] = val
        p = pos[idx] // 2
        
        while p:
            mid = (ls[p] + rs[p]) // 2
            seg_tree[p] = seg_tree[2 * p] + seg_tree[2 * p + 1] + (nums[mid] > nums[mid + 1])
            if seg_tree[p] == 0: dp[p] = rs[p] - ls[p] + 1
            else: dp[p] = (dp[2 * p] + dp[2 * p + 1]) * rev2 % mod
            p //= 2
        
        outs.append(dp[1])
    
    print('\n'.join(map(str, outs)))