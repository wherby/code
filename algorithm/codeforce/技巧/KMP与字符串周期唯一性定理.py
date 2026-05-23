# https://codeforces.com/gym/106540/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/05/0522/solution/cf106540a.md
# 为了不让前缀连接的字符串有重合，必须使用KMP[j]==0的长度的前缀拼接，因为kmp[j]==0 表示了当前位置结束的后缀字符串与当前字符串没有相同的前缀串
#

import init_setting
from cflibs import *
from lib.kmp import *
def main():
    t = II()
    outs = []
    
    mod = 998244353
    
    for _ in range(t):
        n, k = MII()
        kmp = prep(I())
        
        dp = [0] * (k + 1)
        dp[0] = 1
        
        for i in range(k):
            for j in range(n):
                if kmp[j] == 0 and i + j + 1 <= k:
                    dp[i + j + 1] = (dp[i + j + 1] + dp[i]) % mod
        
        outs.append(dp[k])
    
    print('\n'.join(map(str, outs)))

main()