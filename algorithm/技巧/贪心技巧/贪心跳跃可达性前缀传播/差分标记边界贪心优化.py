# https://codeforces.com/gym/106764/problem/H
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1017/solution/cf106764h.md
# 在分标记的时候，需要知道当前点可以取得的最右有效区域
# 这里在差分标记的时候从左到右遍历差分，就可以在最左需要的时候优先处理
# 对于当前区域最右的覆盖。利用贪心覆盖可以把这个值往后传递

import init_setting
from cflibs import *
def main():
    n, k = MII()
    nums = LII()
    radius = LII()
    
    farthest = [0] * n
    
    for i in range(n):
        l = fmax(0, i - radius[i])
        r = fmin(n - 1, i + radius[i])
        farthest[l] = fmax(farthest[l], r)
    
    for i in range(1, n):
        farthest[i] = fmax(farthest[i], farthest[i - 1])
    
    diff = [0] * (n + 1)
    
    l, r = 1, 2 * 10 ** 9
    
    while l <= r:
        mid = (l + r) // 2
        
        cur = 0
        total = 0
        flg = True
        
        for i in range(n):
            cur += diff[i]
            v = fmax(mid - (nums[i] + cur), 0)
            
            diff[farthest[i] + 1] -= v
            cur += v
            total += v
            
            if total > k:
                flg = False
                break
        
        for i in range(n + 1):
            diff[i] = 0
        
        if flg: l = mid + 1
        else: r = mid - 1
    
    print(r)