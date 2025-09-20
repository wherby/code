# https://codeforces.com/gym/104059/problem/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0919/solution/cf104059j.md
# 直接枚举可能的最终花色排序顺序，然后用DP计算在顺序中最大可能的数量
# 每次计算当前值的转移，然后再滚动转移状态


import init_setting
from cflibs import *
def main():
    s = I()
    ans = 0
    
    for p in permutations('hdcs'):
        dp = [0] * 4
        for c in s:
            dp[p.index(c)] += 1
            dp[1] = fmax(dp[1], dp[0])
            dp[2] = fmax(dp[2], dp[1])
            dp[3] = fmax(dp[3], dp[2])
        ans = fmax(ans, dp[3])
    
    print(len(s) - ans)