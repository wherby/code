# https://codeforces.com/gym/105833/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1001/solution/cf105833c.md
# 从右到左的状态转移
# 为什么不考虑在i 点 “选或者不选” 的状态转移
# 因为状态定义为 dp[i][j] 为 在i点有j的累计伤害值的状态
# 因为背包从大到小，对于大的状态不会有重复选择的问题，
#  fmax(dp[nj], dp[j] - cs[i]) 在这里就解决了选或者不选的转移状态




import init_setting
from lib.cflibs import *
def main():
    n = II()
    hs = LII()
    ds = LII()
    cs = LII()
    
    inf = 10 ** 9
    dp = [-inf] * 5001
    
    dp[0] = 0
    
    for i in range(n - 1, -1, -1):
        for j in range(5000, -1, -1):
            nj = fmin(j + ds[i], 5000)
            dp[nj] = fmax(dp[nj], dp[j] - cs[i])
        
        for j in range(5001):
            dp[j] += fmin(j, hs[i])
    
    print(max(dp))