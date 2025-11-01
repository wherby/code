# algorithm/codeforce/技巧/递增数列背包DP技巧.py
# 已知一个递增数列和为M，求不同长度的情况下有多少种排列

M =100
N =10

dp = [[0]*(M+1) for _ in range(N+1)]
dp[0][0] =1 
mod = 10**9+7
for i in range(1,N+1):
    for j in range(M+1):
        dp[i][j] +=dp[i-1][j]
        if j >= i:
            dp[i][j] += dp[i][j-i]
        dp[i][j] %= mod 
print(dp[-1])

from functools import cache
@cache
def dfs(idx,res,last):
    if idx ==N:
        if res ==0:
            return 1
        else:
            return 0 
    ret =0
    for j in range(last,res+1):
         ret += dfs(idx +1, res -j, j)
    return ret%mod

ans = []
for i in range(M+1):
    ans.append(dfs(0,i,0))
print(ans)