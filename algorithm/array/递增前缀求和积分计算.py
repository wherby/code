# https://codeforces.com/gym/103708/problem/L
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1011/solution/cf103708l.md
# 在一个数列中，以nums[i]为最大值的子序列，求所有以nums[i]为最大值的子序列的序列和之和
# 在子序列中 nums[i]为最大值的序列数量由左右序列构成，
#  左右序列分别来看共享的时候，会形成两个不等高(高度为左右影响的长度)中间到两边递减为1三角形，
#  然后用acc2构造一个递增为1的前缀三角形数列，可以用前缀三角形的差 和前缀和的差的差值获得左右两个递减三角形的共享和
# algorithm/codeforce/技巧/递增前缀求和积分计算.py

import init_setting
from cflibs import *
def main():
    n = II()
    nums = LII()
    mod = 10 ** 9 + 7
    
    acc1 = list(accumulate(nums, initial=0))
    acc2 = list(accumulate((i * nums[i] % mod for i in range(n)), initial=0))
    
    left = [0] * n
    stk = [-1]
    
    for i in range(n):
        while stk[-1] != -1 and nums[stk[-1]] <= nums[i]:
            stk.pop()
        left[i] = stk[-1]
        stk.append(i)
    
    right = [0] * n
    stk = [n]
    
    for i in range(n - 1, -1, -1):
        while stk[-1] != n and nums[stk[-1]] <= nums[i]:
            stk.pop()
        right[i] = stk[-1]
        stk.append(i)
    
    ans = 0
    
    for i in range(n):
        ans += nums[i] * (i - left[i]) % mod * (right[i] - i) % mod
        ans %= mod
        
        ans += (acc2[i] - acc2[left[i] + 1] - (acc1[i] - acc1[left[i] + 1]) * left[i]) % mod * (right[i] - i) % mod
        ans %= mod
        
        ans += ((acc1[right[i]] - acc1[i + 1]) * right[i] - (acc2[right[i]] - acc2[i + 1])) % mod * (i - left[i]) % mod
        ans %= mod
    
    print(ans)

main()
