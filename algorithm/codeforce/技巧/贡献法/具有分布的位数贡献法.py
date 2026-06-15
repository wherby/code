# https://codeforces.com/gym/102441/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0608/solution/cf102441f.md
# 题目中要求 S**2 的期望值，S由N个数的异或而成
# S的平方数可以用 S中每一位的期望概率求得乘积的贡献和。
# 然而单独求每一位的 0,1 期望，是可以求出来的，但是由于一个数字的每位的0,1分布会整体影响了各单独位置的分布。所以用每一位分离的观点看分布不是独立的，所以求平方数的时候不能直接乘积
# 所以需要用乘积的位数分布来计算，而N个数字的异或，则是乘积位数分布的DP结果。
# 在概率求save[i]的时候，是求有i个置位数字的情况下，分布总结果是有奇数个元素被选中的概率，这样就把概率的分布压缩成了奇数个和偶数个的分布



import init_setting
from cflibs import *
def main():
    mod = 10 ** 9 + 7
    
    n, x, y = MII()
    nums = LII()
    
    v1 = x * pow(y, -1, mod) % mod
    v0 = (mod + 1 - v1) % mod
    
    cnt = [[0] * 900 for _ in range(4)]
    
    for v in nums:
        vals = [v >> i & 1 for i in range(30)]
        
        for i in range(30):
            for j in range(30):
                cnt[vals[i] * 2 + vals[j]][i * 30 + j] += 1
    
    p0, p1 = 1, 0
    saved = [0] * (n + 1)
    
    for i in range(1, n + 1):
        p0, p1 = (p0 * v0 + p1 * v1) % mod, (p1 * v0 + p0 * v1) % mod
        saved[i] = p1
    
    ans = 0
    
    for i in range(30):
        for j in range(30):
            dp = [0] * 4
            dp[0] = 1
            
            for vi in range(2):
                for vj in range(2):
                    v = vi * 2 + vj
                    x = cnt[v][i * 30 + j]
                    
                    p1 = saved[x]
                    p0 = (mod + 1 - p1) % mod
                    
                    ndp = [0] * 4
                    
                    for idx in range(4):
                        ndp[idx] = (dp[idx ^ v] * p1 + dp[idx] * p0) % mod
                    
                    dp = ndp
            
            ans += (1 << i + j) % mod * dp[3] % mod
            ans %= mod
    
    print(ans)