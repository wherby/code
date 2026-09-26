# https://codeforces.com/gym/106718/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0925/solution/cf106718c.md
# 因为收益函数是分段函数，这里采用把全局都先减去一个值变成常数，然后再加回最大可能的不减部分，把分段函数的两个部分在”两个不同的区间计算“，最终的结果其实是可以合并的
# algorithm/codeforce/dp/docs/先弃后取解决分段函数.md
# # (ma2 if dp[i][j] == ma1 else ma1) + x * ks[j]) 这里是保证所谓的下一段递推区间的起点的最大值不是j结束的

import init_setting
from cflibs import *
def main():
    n, z = MII()
    
    ks = [0]
    ds = [1]
    xs = [0]
    
    for _ in range(n):
        k, d, x = MII()
        ks.append(k)
        ds.append(d)
        xs.append(x)
    
    dp = [[0] * (n + 1) for _ in range(z + 1)]
    
    for i in range(z):
        ma1 = 0
        ma2 = 0
        
        for j in range(n + 1):
            dp[i + 1][j] = fmax(dp[i + 1][j], dp[i][j] + ks[j] - xs[j])
            
            if dp[i][j] > ma1: ma1, ma2 = dp[i][j], ma1
            elif dp[i][j] > ma2: ma2 = dp[i][j]
        
        for j in range(n + 1):
            nd = fmin(z - i, ds[j])
            
            for x in range(1, nd + 1):
                dp[i + x][j] = fmax(dp[i + x][j], (ma2 if dp[i][j] == ma1 else ma1) + x * ks[j])
    
    print(max(dp[z]))