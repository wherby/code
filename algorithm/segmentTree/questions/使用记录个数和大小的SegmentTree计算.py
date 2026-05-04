# https://codeforces.com/gym/106501/problem/K
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0429/solution/cf106501h.md
# 因为等级需要递增，而等级的个数就2个，所以可以遍历等级的分界线找到最大的长度
# 在分界线两边合法的正数可以贪心取
# 处理负数的时候会优先级，所以把数按照从大到小排序，把负数的数字放入segmentTree计算当前的正数能cover最多多少个负数
# 对于负数大小和负数个数，采用两个Segment Tree记录



import init_setting
from cflibs import *
from lib.segTreeWithFindFirst import SegTree
def main():
    n, k = MII()
    nums = LII()
    
    for i in range(n):
        nums[i] -= k
    
    tags = LII()
    
    st_range = sorted(range(n), key=lambda x: -nums[x])
    pos = [0] * n
    
    for i in range(n):
        pos[st_range[i]] = i
    
    seg = SegTree(add, 0, n)
    seg_cnt = SegTree(add, 0, n)
    
    total = 0
    cnt = 0
    
    for i in range(n):
        if tags[i] == 2:
            if nums[i] >= 0:
                total += nums[i]
                cnt += 1
            else:
                seg.set(pos[i], -nums[i])
                seg_cnt.set(pos[i], 1)
    
    p = seg.max_right(0, lambda x: x <= total)
    ans = cnt + seg_cnt.prod(0, p)
    
    for i in range(n):
        if tags[i] == 1:
            if nums[i] >= 0:
                total += nums[i]
                cnt += 1
            else:
                seg.set(pos[i], -nums[i])
                seg_cnt.set(pos[i], 1)
        else:
            if nums[i] >= 0:
                total -= nums[i]
                cnt -= 1
            else:
                seg.set(pos[i], 0)
                seg_cnt.set(pos[i], 0)
    
        p = seg.max_right(0, lambda x: x <= total)
        ans = fmax(ans, cnt + seg_cnt.prod(0, p))
    
    print(ans)
