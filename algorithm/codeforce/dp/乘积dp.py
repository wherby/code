
# https://codeforces.com/problemset/problem/2060/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0718/solution/cf2060f.md
# 先求出除去大于1的因子乘积为x的数长度为m的个数,因为x的值为10**5，所以最大的长度为17 
# 然后把m个数放在m:n个的总和为 C(m,m) +C(m,m+1) + C(m,m+2) + ... + C(m,n) = C(m+1,n+1)
# 上面这个求和也可以表示为 n 个位置，加上最后一个停止位置，一共有n+1个位置可以选择，并且选择m个位置，在m个位置后再选一个停止位，就是m+1个位置，所以和的最终值表示为 : C(m+1,n+1) 

import init_setting
from cflibs import *
from lib.combineWithPreCompute import *
def main():
    K, mod = 10 ** 5, 998244353
    dp = [[0] * (K + 1) for _ in range(17)]
    
    dp[0][1] = 1
    
    for i in range(16):
        for j in range(K + 1):
            if dp[i][j]:
                for v in range(2 * j, K + 1, j):
                    dp[i + 1][v] += dp[i][j]
                    if dp[i + 1][v] >= mod:
                        dp[i + 1][v] -= mod
    
    f = Factorial(20, mod)
    
    t = II()
    outs = []
    
    for _ in range(t):
        k, n = MII()
        
        ans = [0] * k
        ans[0] = n
    
        for i in range(2, k + 1):
            cur = 1
            for j in range(17):
                cur = cur * (n + 1 - j) % mod
                ans[i - 1] += dp[j][i] * cur % mod * f.fac_inv(j + 1) % mod
                if ans[i - 1] >= mod:
                    ans[i - 1] -= mod
        
        outs.append(' '.join(map(str, ans)))
    
    print('\n'.join(outs))

main()