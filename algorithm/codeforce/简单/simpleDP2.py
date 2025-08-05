# https://codeforces.com/problemset/problem/18/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0731/solution/cf18d.md
# 状态转移， 只有sell的时候，才会触发状态转移
# 对于win的时候，记录了last[x]的变化，这个值被应用于状态转移


import init_setting
from lib.cflibs import *
def main():
    last = [-1] * 2005
    n = II()

    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        s, x = LI()
        x = int(x)
        
        dp[i] = dp[i - 1]
        
        if s[0] == 'w':
            last[x] = i - 1
        else:
            if last[x] != -1:
                dp[i] = fmax(dp[i], dp[last[x]] + (1 << x))

    print(dp[n])