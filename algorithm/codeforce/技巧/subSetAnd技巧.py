# https://codeforces.com/gym/104671/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1113/solution/cf104671f.md
# 取的数字是subset, 如果不包含k则没有用，用全1 表示，否则把k去除，然后看区间能不能and成 0



import init_setting
from cflibs import *
def main(): 
    n, k, q = MII()
    nums = LII()
    
    tmp = [-1] * n
    
    for i in range(n):
        if nums[i] & k == k:
            tmp[i] = nums[i] - k
    
    seg = SegTree(iand, -1, tmp)
    
    outs = []
    for _ in range(q):
        l, r = GMI()
        outs.append('NO' if seg.prod(l, r + 1) else 'YES')
    
    print('\n'.join(outs))