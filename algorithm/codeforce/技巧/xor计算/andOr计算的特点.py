# https://codeforces.com/gym/106607/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0703/solution/cf106607f.md
# 满足条件的数字and or 前后缀计算的时候对置位有要求
# 变成了数位DP，这里用递推的方式计算数位DP更块？  algorithm/dp/dpWithStatus-Number/数位DP/数位DP的递推形式



import init_setting
from lib.cflibs import *
def main():
    t = II()
    outs = []
    
    mod = 998244353
    
    for _ in range(t):
        n, m = MII()
        m += 1
    
        dp = [0] * 60
        c = 0
        
        for i in range(59, -1, -1):
            for j in range(58, -1, -1):
                dp[j + 1] += dp[j]
            if m >> i & 1:
                dp[c] += 1
                c += 1
        
        ans = 0
        for i in range(60):
            ans += dp[i] % mod * pow(n, i, mod) % mod
            ans %= mod
        
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))