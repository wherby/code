# https://codeforces.com/gym/105761/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/12/1223/solution/cf105761f.md
# 状态设计 DP[i][j] 表示第i次中毒，第j次测试能测试出最大多少个餐馆的数量， 但是没有任何选择策略被设置
#  状态转移：dp[i][0] = 1 边界条件，如果只测试一次，则最多可以确定1个餐馆就是目标
#          dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]  表示两种情况，中毒和非中毒的情况。这里其实就暗含了餐厅选择策略，
#               dp[i - 1][j - 1] < dp[i][j - 1], 因为题目里有 in worse case,所以，单次选择的餐厅数目为 dp[i - 1][j - 1]  如果中毒就继续在这些选择中用 i-i 次中毒 j-1次测试找到目标，反之则在另外的区域找到目标

import init_setting
from cflibs import *
def main(): 
    n, p = MII()
    
    p = fmin(p, 20)
    dp = [[0] * (n + 1) for _ in range(p + 1)]
    
    for i in range(n + 1):
        dp[0][i] = 1
    
    inf = 10 ** 9
    for i in range(1, p + 1):
        dp[i][0] = 1
        
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
            dp[i][j] = fmin(dp[i][j], inf)
    
    for i in range(n + 1):
        if dp[p][i] >= n:
            print(i)
            break