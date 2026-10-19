# https://codeforces.com/gym/102307/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1009/solution/cf102307c.md
# 边界约束的LCS


import init_setting
from cflibs import *
def main():
    s1 = [ord(c) for c in I()]
    s2 = [ord(c) for c in I()]
    
    n = len(s1)
    bound = n // 100
    
    dp = [0] * (n + 1)
    
    for i in range(n):
        l = fmax(0, i - bound)
        r = fmin(n - 1, i + bound)
        
        for j in range(r, l - 1, -1):
            if s1[i] == s2[j]:
                dp[j + 1] = dp[j] + 1
        
        for j in range(l, r + 1):
            dp[j + 1] = fmax(dp[j + 1], dp[j])
    
    print('Long lost brothers D:' if dp[n] >= n - bound else 'Not brothers :(')