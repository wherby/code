# https://codeforces.com/gym/105698/problem/I
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1118/solution/cf105698i.md
# 非三角形的个数的数组本身就是求LIS的变形
# 前缀和 与 DP的关系
# dp_acc[i][j] 表示选择j点为次大边时候，最小边到i的前缀和 对于此选择同时也是dp[i][j]的转移目的，因为dp[i][j] 表示用i,j 作为次大和最大边的时候，不能构成三角形的数量
# 

import init_setting
from cflibs import *
def main(): 
    n = II()
    nums = LII()
    nums.sort()
    
    mod = 998244353
    
    dp = [[0] * n for _ in range(n)]
    dp_acc = [[0] * n for _ in range(n)]
    
    for i in range(n):
        pos = 0
        for j in range(i + 1, n):
            while pos < i and nums[i] + nums[pos] <= nums[j]:
                pos += 1
            
            if pos: dp[i][j] = dp_acc[pos - 1][i]
            dp[i][j] += 1
            dp[i][j] %= mod
            
            if i: dp_acc[i][j] = dp_acc[i - 1][j]
            dp_acc[i][j] += dp[i][j]
            dp_acc[i][j] %= mod
    
    ans = 0
    for x in dp:
        for y in x:
            ans += y
    
    print((ans + n) % mod)