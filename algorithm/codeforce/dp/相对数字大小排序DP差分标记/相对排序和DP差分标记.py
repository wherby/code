# https://codeforces.com/gym/106363/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0213/solution/cf106363f.md
# 如果记录取值和剩余数字，则复杂度太大，所以只需要记录最后一个数字的相对位置即可
# 如果DP转移的时候，遍历每个数字，则状态转移会增加N被，这里用差分标记，记录当前状态可能的转移
# 然后在下一轮的时候，进行前缀和计算，得到每个状态的转移结果，这样就避免了在转移的时候增加N倍的复杂度


import init_setting
from cflibs import *
def main(): 
    mod = 10 ** 9 + 7
    n, k = MII()
    
    def f(i, j):
        return i * (n + 1) + j
    
    dp = [[0] * (n + 1) * (n + 1) for _ in range(4)]
    ndp = [[0] * (n + 1) * (n + 1) for _ in range(4)]
    
    for i in range(n):
        dp[1][f(i, 0)] = 1
    
    for i in range(n - 1):
        for x in range(1, 4):
            for y in range(n - i):
                for z in range(fmax(i - 2, 0) + 1):
                    ndp[1][f(0, z)] += dp[x][f(y, z)]
                    ndp[1][f(y, z)] -= dp[x][f(y, z)]
                    if x < 3:
                        ndp[x + 1][f(y, z)] += dp[x][f(y, z)]
                        ndp[x + 1][f(n - 1 - i, z)] -= dp[x][f(y, z)]
                    else:
                        ndp[3][f(y, z + 1)] += dp[x][f(y, z)]
                        ndp[3][f(n - 1 - i, z + 1)] -= dp[x][f(y, z)]
        
        i += 1
        for x in range(1, 4):
            for y in range(n - i):
                for z in range(fmax(i - 2, 0) + 1):
                    ndp[x][f(y + 1, z)] += ndp[x][f(y, z)]
                    dp[x][f(y, z)] = ndp[x][f(y, z)] % mod
                    ndp[x][f(y, z)] = 0
    
    ans = 0
    for x in range(4):
        ans += dp[x][f(0, k)]
        ans %= mod
    
    print(ans)