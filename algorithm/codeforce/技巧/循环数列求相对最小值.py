# https://codeforces.com/gym/106054/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1029/solution/cf106054b.md
# B数列的 i，会对A初始序列i, i+k  位置 的最小值有限制 所以以 k循环，初始序列的数字有最小值限制
# 为了求 “水位” 线， 假设 A[0]为0，得到相对水位数值，找打最低水位就是初始水位的最小值

import init_setting
from cflibs import *
def main(): 
    n, k = MII()
    nums = LII()
    mod = 998244353
    
    tmp = [0] * n
    
    for i in range(k, n):
        tmp[i] = tmp[i - k] + nums[i - k + 1] - nums[i - k]
    
    to_add = 0
    for i in range(k):
        val = 0
        for j in range(i, n, k):
            val = fmin(val, tmp[j])
        to_add -= val
    
    if to_add > nums[0]:
        print(0)
    else:
        tot = nums[0] - to_add
        v1 = 1
        v2 = 1
        
        for i in range(1, k):
            v1 = v1 * (tot + k - i) % mod
            v2 = v2 * i % mod
        
        print(v1 * pow(v2, -1, mod) % mod)