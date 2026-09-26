# https://codeforces.com/gym/105223/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0902/solution/cf105223g.md
# 对于任意一个子数组求子数组内的和
# 按照贡献法，需要求 i 等于 1 到k 个 奇数个1 的子数组 和 j 等于 0 到 n-k个0 的子数组，此子数组贡献是 1<<(i+j-1)  
# 这里是2阶2项式求和，可以拆为两个二项式线性无关的项
# algorithm/codeforce/docs/数论/二阶2项式定理利用.md

import init_setting
from cflibs import *
def main():
    n = II()
    nums = LII()
    
    cnt = [0] * 30
    
    for x in nums:
        for i in range(30):
            cnt[i] += x >> i & 1
    
    mod = 10 ** 9 + 7
    pw3 = [1] * (n + 1)
    
    for i in range(n):
        pw3[i + 1] = pw3[i] * 3 % mod
    
    rev2 = (mod + 1) // 2
    
    q = II()
    outs = []
    
    for _ in range(q):
        idx, val = MII()
        idx -= 1
        
        for i in range(30):
            cnt[i] -= nums[idx] >> i & 1
    
        nums[idx] = val
        
        for i in range(30):
            cnt[i] += nums[idx] >> i & 1
        
        ans = 0
        
        for i in range(29, -1, -1):
            ans = (ans * 2 + (pw3[n] - pw3[n - cnt[i]])) % mod
        
        outs.append(ans * rev2 % mod)
    
    print('\n'.join(map(str, outs)))