# https://codeforces.com/gym/105316/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/12/1201/solution/cf105316a.md
# 枚举可能的几何图形分割
# 关键是找到一条大于一半周长的边：
# ans = pw2[n - 1] - 1   1表示二进制的时候全0，这时候只有一条边是不合法的
# 但是如果图形分割的时候，有只有两条边，这种情况是在哪里被去除的？ 
# 在枚举左右边长边的时候，如果只有两条边，则左，右边必然是长边，所以在这里就把2条边的情况包含了；
#   ans += 1 这是左右长边枚举的时候，都会互相包含，所以再加回去
    # cur = 0
    # for i in range(n - 1):
    #     cur += nums[i]
    #     if cur * 2 >= total:
    #         ans -= pw2[n - 2 - i]
    #         ans %= mod
        
    #     if cur * 2 == total:
    #         ans += 1
    #         ans %= mod
    
    # cur = 0
    # for i in range(n - 1, 0, -1):
    #     cur += nums[i]
    #     if cur * 2 >= total:
    #         ans -= pw2[i - 1]
    #         ans %= mod
#

import init_setting
from lib.cflibs import *

def main(): 
    mod = 10 ** 9 + 7
    
    n = II()
    nums = LII()
    
    pw2 = [1] * n
    for i in range(1, n):
        pw2[i] = pw2[i - 1] * 2 % mod
    
    total = sum(nums)
    
    ans = pw2[n - 1] - 1
    
    cur = 0
    for i in range(n - 1):
        cur += nums[i]
        if cur * 2 >= total:
            ans -= pw2[n - 2 - i]
            ans %= mod
        
        if cur * 2 == total:
            ans += 1
            ans %= mod
    
    cur = 0
    for i in range(n - 1, 0, -1):
        cur += nums[i]
        if cur * 2 >= total:
            ans -= pw2[i - 1]
            ans %= mod
    
    l, r = 0, 0
    cur = 0
    
    while l < n:
        while r < n and cur * 2 < total:
            cur += nums[r]
            r += 1
        
        if l > 0 and r < n:
            ans -= pw2[l - 1] * (pw2[n - r] - 1) % mod
            ans %= mod
        
        cur -= nums[l]
        l += 1
    
    print(ans)

main()