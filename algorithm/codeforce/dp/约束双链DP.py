# https://codeforces.com/gym/103102/problem/I
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0613/solution/cf103102i.md
# algorithm/codeforce/dp/docs/约束双链DP.md
# 需要有两个递减链，其中每个链满足 q[i]%q[i+1] <=2 ,
# 这里是枚举其中一条链的最大值为DP[i]的时候的转移，因为要假设中间有段连续空间被另一条链抽去了，所以j是另一条链抽去的最大值，随着DP转移，另一条链的最大值也是被枚举的目标
# 因为 for i in range(3, n)，这里在i递推的时候，假设i为单链最大值的情况已经计算完了，所以也可以把这个结果加入




import init_setting
from lib.cflibs import *
def main():
    n = II()
    mod = 10 ** 9 + 7
    
    if n < 3:
        print(n)
    else:
        dp = [1] * (n + 1)
        
        for i in range(3, n):
            dp[n] += dp[i]
            dp[n] %= mod
            
            for j in range(2 * i - 1, n, i):
                dp[j] += dp[i]
                dp[j] %= mod
            
            for j in range(2 * i, n, i):
                dp[j] += dp[i]
                dp[j] %= mod
            
            for j in range(i + 1, n, i):
                dp[j] += dp[i]
                dp[j] %= mod
        
        print(dp[n] * 2 * n % mod)