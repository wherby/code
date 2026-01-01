# https://codeforces.com/gym/105948/problem/H
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/12/1231/solution/cf105948h.md
# 原题求概率相关的问题
# 求任意组合的K个数字里，大于平均数字的期望个数
# 对于任意的K，大于平均数的期望个数，这就是贡献法计算，对于每个数字而言，再取 K-1 个数字，组成的平均数比当前数字小即可
# 然而对于整体数字的分布用 DP[i][j] 表示有 i 个数 组成和为 j的子数组 的个数
# 对于任意数字为V而言，需要找到不包含它的数字 k-1 时候，组成的平均数字小于  (k-1)*V的个数，这时就需要用到背包回退技巧
# algorithm/codeforce/docs/背包回退运算顺序.md



import init_setting
from cflibs import *
from lib.combineWithPreCompute import *
def main(): 
    n = II()
    nums = LII()
    
    mod = 998244353
    
    f = Factorial(n, mod)
    
    dp = [[0] * (n * n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    for i in range(n):
        for j in range(i, -1, -1):
            for k in range(n * n + 1):
                if dp[j][k]:
                    dp[j + 1][k + nums[i]] += dp[j][k]
                    dp[j + 1][k + nums[i]] %= mod
    
    ans = [0] * (n + 1)
    
    for v in nums:
        for j in range(n):
            for k in range(n * n + 1):
                if dp[j][k]:
                    dp[j + 1][k + v] -= dp[j][k]
                    dp[j + 1][k + v] %= mod
        
        for j in range(1, n):
            for k in range(n * n + 1):
                if j * v > k:
                    ans[j + 1] += dp[j][k]
                    ans[j + 1] %= mod
        
        for j in range(n - 1, -1, -1):
            for k in range(n * n + 1):
                if dp[j][k]:
                    dp[j + 1][k + v] += dp[j][k]
                    dp[j + 1][k + v] %= mod
    
    for i in range(2, n + 1):
        ans[i] = ans[i] * f.combi_inv(n, i) % mod * f.inv(i) % mod
    print(ans[2:])

main()