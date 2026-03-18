# https://codeforces.com/gym/106407/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0309/solution/cf106407b.md
# 按照题目要求化简出来的各项式的值，发现是一个求全排列奇偶相等的排列的个数，
# 这个题目的核心是求全排列奇偶相等的排列的个数
# 则用背包DP 求出奇偶位相等的组合个数



import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    mod = 10 ** 9 + 7
    
    for _ in range(t):
        n = II()
        if n * (n + 1) // 2 % 2: outs.append(0)
        else:
            M = n * (n + 1) // 4
            dp = [[0] * (M + 1) for _ in range(n // 2 + 2)]
            dp[0][0] = 1
            
            for x in range(n + 1):
                for i in range(n // 2 + 1, 0, -1):
                    for j in range(x, M + 1):
                        dp[i][j] += dp[i - 1][j - x]
                        dp[i][j] %= mod
            
            n += 1
            ans = dp[n // 2][M] + dp[n - n // 2][M]
            ans = ans * (mod + 1) // 2 % mod
            
            for x in range(1, n // 2 + 1):
                ans = ans * x % mod
            
            for x in range(1, n - n // 2 + 1):
                ans = ans * x % mod
            
            outs.append(ans)
    
    print('\n'.join(map(str, outs)))