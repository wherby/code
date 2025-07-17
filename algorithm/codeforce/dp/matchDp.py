# https://codeforces.com/problemset/problem/223/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0716/solution/cf223a.md
# 括号匹配DP，设置初始值

import sys
sys.path.append("..")
from cflibs.cflibs import *
def main():
    s = I()
    n = len(s)
    
    dp = list(range(1, n + 1))
    
    for i in range(1, n):
        if s[i] == ')':
            pos = dp[i - 1]
            if pos and s[pos - 1] == '(':
                dp[i] = pos - 1 if pos - 1 == 0 else dp[pos - 2]
        elif s[i] == ']':
            pos = dp[i - 1]
            if pos and s[pos - 1] == '[':
                dp[i] = pos - 1 if pos - 1 == 0 else dp[pos - 2]
    
    acc = [0] * (n + 1)
    for i in range(n):
        acc[i + 1] = acc[i]
        if s[i] == '[':
            acc[i + 1] += 1
    
    res = 0
    idx = 0
    
    for i in range(n):
        if acc[i + 1] - acc[dp[i]] > res:
            res = acc[i + 1] - acc[dp[i]]
            idx = i
    
    print(res)
    print(s[dp[idx]:idx+1])