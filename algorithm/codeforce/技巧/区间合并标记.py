# https://codeforces.com/gym/105187/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/12/1203/solution/cf105187b.md
# 假设 一组对象 x,y 且 x<=y
# 对于结果有多重情况   (x+3,y), (x+1,y+1),(x,y+3)
# 但是对于另外的人值为Z， 关心这组对象的两个点是在  [0，Z+3] 内，越多越好
# 当有一个点的时候，最小值就是 x,  而有两个点在区间内，最小值为 min( max(x+3,y),y+1)
# 就可以用上面的分析在线段树上标记

import init_setting
from cflibs import *
from lib.fenwicktree import *
def main(): 
    n = II()
    nums = LII()
    xs = []
    ys = []
    
    for _ in range(n):
        x, y = MII()
        xs.append(x)
        ys.append(y)
    
    M = 5 * 10 ** 5 + 100
    fen = FenwickTree(M)
    
    for i in range(n):
        x, y = nums[xs[i]], nums[ys[i]]
        
        if x > y:
            x, y = y, x
        
        fen.add(x, 1)
        fen.add(fmin(fmax(x + 1, y + 1), fmax(x + 3, y)), 1)
    
    ans = [0] * (2 * n)
    
    for i in range(n):
        x, y = nums[xs[i]], nums[ys[i]]
        
        if x > y:
            x, y = y, x
        
        fen.add(x, -1)
        fen.add(fmin(fmax(x + 1, y + 1), fmax(x + 3, y)), -1)
        
        ans[xs[i]] = 2 * n - fen.rsum(0, nums[xs[i]] + 3)
        ans[ys[i]] = 2 * n - fen.rsum(0, nums[ys[i]] + 3)
        
        if nums[xs[i]] + 3 >= nums[ys[i]]: ans[xs[i]] -= 1
        if nums[ys[i]] + 3 >= nums[xs[i]]: ans[ys[i]] -= 1
        
        fen.add(x, 1)
        fen.add(fmin(fmax(x + 1, y + 1), fmax(x + 3, y)), 1)
    
    print(' '.join(map(str, ans)))

main()