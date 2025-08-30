# https://codeforces.com/problemset/problem/1989/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0823/solution/cf1989e.md
# 这里特殊的点是如果在中间的时候，2的长度变成2个1的长度的段是不会增加B的数量的，但是在两边却是可以增加的，所以DP的时候，两边要求2的长度的转移，中间不求
# 然而对于状态总数，只是求在n长度的条件下，大于k段长度的所有B的个数
# 因为大于k段时候，所以在k那里会有自身转移，
# dp[j][i] 表示有i个元素的时候，有j个段的数量
# dp_acc[j][i] = sum(dp[j][k] (k<=i))
# 所以跳过长度为2的状态转移就是  dp[j][i] = dp[j-1][i-1] + dp_acc[j-1][i-3]
# dp_acc[j][i] = dp_acc[j][i-1] + dp[j][i] (定义)
# 因为开始和结尾段需要2长度的转移，而开始段因为dp_acc已经包含了
# 所以在求结尾段的时候， dp[k][n] + dp[k-1][n-2] + dp[k][n-2] 




import init_setting
from cflibs import *

def main():
    n, k = MII()
    mod = 998244353
    
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    dp_acc = [[0] * (n + 1) for _ in range(k + 1)]
    
    for i in range(1, n + 1):
        dp[1][i] = 1
        dp_acc[1][i] = i
        
        for j in range(2, k + 1):
            dp[j][i] = dp[j - 1][i - 1]
            if i >= 3:
                dp[j][i] += dp_acc[j - 1][i - 3]
                dp[j][i] %= mod
            dp_acc[j][i] = (dp_acc[j][i - 1] + dp[j][i]) % mod
        
        dp[k][i] += dp[k][i - 1]
        dp[k][i] %= mod
        
        if i >= 3:
            dp[k][i] += dp_acc[k][i - 3]
            dp[k][i] %= mod
        
        dp_acc[k][i] = (dp_acc[k][i - 1] + dp[k][i]) % mod
    
    print((dp[k][n] + dp[k - 1][n - 2] + dp[k][n - 2]) % mod)