# https://codeforces.com/gym/106178/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1121/solution/cf106178b.md
# 对于next dp 能到的状态值，是在[start,end]里能被 i 整除的数字， 所以left = (start +i-1)//i 需要上取整，使得整除树在区间内
# 而对于影响的idx [l,r]， 采用差分标记方式，可以节约计算时间
# fmin(n, k) 是出于对值域判断，因为 [start,end] 可以表述为 [j*(i-1)+1, j*(i-1)+k] 的区间内能整除 i的个数， 如果 i>k,则此区间长度最大为k,整除 i的个数最多为1， 而 k 取 j一样大，则一定整除，则至少有一个可以整除
# 所以 只需循环最多k次


import init_setting
from cflibs import *
def main(): 
    n, k = MII()
    mod = 998244353
    
    n = fmin(n, k)
    
    dp = [0] * (k + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        ndp = [0] * (k + 1)
        
        for j in range(k + 1):
            start = j * (i - 1) + 1
            end = j * (i - 1) + k
            
            left = (start + i - 1) // i
            right = end // i
            
            ndp[left] += dp[j]
            if right < k:
                ndp[right + 1] -= dp[j]
        
        for j in range(1, k + 1):
            ndp[j] += ndp[j - 1]
            ndp[j] %= mod
        
        dp = ndp
    
    print(sum(dp) % mod)