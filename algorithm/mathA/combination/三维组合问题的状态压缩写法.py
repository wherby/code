# https://codeforces.com/gym/105745/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0415/solution/cf105745e.md
# 这里有 i,j,k,cur=[0,1,2] 4个变量，如果直接写的话 就有300**3 *3的空间需要更新
# 而且在初始状态情况下，边界更难设置
# 这里把i作为循环变量，编码 j,k 这时就只有 300*300 大小，cur表示最后一个是i,j,k 的哪个方向
# 这里在 i==0 的时候就要初始化的原因就是就算i=0, k,j的边界也需要设置
#  dp[1][f(1, 0)] = 1
#  dp[2][f(0, 1)] = 1
# 为了在i ==1 之后 也能从 cur= 0转移过去，在i==0的时候，要设置初始值
#   if i == 0:
#        ndp[0][f(0, 0)] = 1
# 使用 ndp 来强制计算 i 增加的时候的状态值




import init_setting
from lib.cflibs import *
def main():  
    x, y, z = MII()
    mod = 10 ** 9 + 7
    
    M = 301
    
    combs = [[0] * M for _ in range(M)]
    
    for i in range(M):
        combs[i][0] = 1
        combs[i][i] = 1
        
        for j in range(1, i):
            combs[i][j] = (combs[i - 1][j] + combs[i - 1][j - 1]) % mod
    
    def c(x, y):
        if x == y: return 1
        if y < 0 or y > x: return 0
        return combs[x][y]
    
    dp = [[0] * (M * M) for _ in range(3)]
    
    def f(i, j): return i * M + j
    
    dp[1][f(1, 0)] = 1
    dp[2][f(0, 1)] = 1
    
    ans = [0] * (x + y + z)
    
    for i in range(x + 1):
        ndp = [[0] * (M * M) for _ in range(3)]
        
        for j in range(y + 1):
            for k in range(z + 1):
                if i + j + k > 1:
                    if j:
                        dp[1][f(j, k)] = (dp[0][f(j - 1, k)] + dp[2][f(j - 1, k)]) % mod
                    if k:
                        dp[2][f(j, k)] = (dp[0][f(j, k - 1)] + dp[1][f(j, k - 1)]) % mod         
                for cur in range(3):
                    if i or j or k:
                        ans[i + j + k - 1] += dp[cur][f(j, k)] * c(x - 1, i - 1) % mod * c(y - 1, j - 1) % mod * c(z - 1, k - 1) % mod
                        ans[i + j + k - 1] %= mod
                
                ndp[0][f(j, k)] = (dp[1][f(j, k)] + dp[2][f(j, k)]) % mod
        
        if i == 0:
            ndp[0][f(0, 0)] = 1
    
        dp = ndp
    
    print(*ans, sep='\n')