# https://codeforces.com/gym/104020/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0211/solution/cf104020c.md
# 无保存的情况下，状态需要时间期望就是成功路径时间除以成功概率
# 利用DP 查询所有长度保存的时候的最小时间


import init_setting
from cflibs import *
def main(): 
    c, t, r = map(int, input().split())
    p = float(input())
    
    time = [0] * (c + 1)
    
    for i in range(c):
        time[i + 1] = (time[i] + 1 + p * r) / (1 - p)
    
    inf = 10 ** 18
    dp = [inf] * (c + 1)
    dp[0] = 0
    
    for i in range(1, c + 1):
        for j in range(i + 1):
            dp[i] = fmin(dp[i], dp[i - j] + time[j] + t)
    
    print(dp[c])