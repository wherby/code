# https://codeforces.com/problemset/problem/251/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0827/solution/cf251c.md
# 减少余数的操作，最后可以用lcm问题开解决，因为这些减少的数字的lcm快内可以确定有最优解，就是DP值@


import init_setting
from cflibs import *
def main():
    a, b, k = MII()
    block = 360360
    inf = 10 ** 6
    
    ans = 0
    
    if a // block != b // block:
        
        dp = [inf] * (block + 1)
        dp[0] = 0
        
        for i in range(1, block + 1):
            dp[i] = fmin(dp[i], dp[i - 1] + 1)
            for j in range(2, k + 1):
                dp[i] = fmin(dp[i], dp[i - i % j] + 1)
        
        ans += dp[a % block]
        a -= a % block
        
        v = (a - b) // block
        ans += dp[block] * v
        a -= v * block
        
        a -= 1
        ans += 1
    
    a %= block
    b %= block
    
    dp = [inf] * block
    dp[b] = 0
    
    for i in range(b + 1, a + 1):
        dp[i] = fmin(dp[i], dp[i - 1] + 1)
        for j in range(2, k + 1):
            dp[i] = fmin(dp[i], dp[i - i % j] + 1)
    
    ans += dp[a]
    print(ans)