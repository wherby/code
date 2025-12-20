# https://codeforces.com/gym/105845/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/12/1217/solution/cf105845f.md
# dp[n][j] 表示n个数分j段， 在这个顺序里，比较难处理状态转移的问题
# 如果dp[j][n] 从分的次数开始递推则可以利用同余特性得到状态转移

import init_setting
from cflibs import *
def main(): 
    n = II()
    mod = 10 ** 9 + 7
    
    dp = [0] * (n + 1)
    dp[0] = 1
    
    ans = 0
    
    for i in range(1, n + 1):
        ndp = [0] * (n + 1)
        
        cur = [0] * i
        pre = 0
        
        for j in range(n + 1):
            pre = (pre + j) % i
            ndp[j] = cur[pre]
            cur[pre] = (cur[pre] + dp[j]) % mod
        
        dp = ndp
        ans = (ans + dp[n]) % mod
    
    print(ans)

main()