# https://codeforces.com/gym/106457/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0408/solution/cf106463f.md
# 分析MEX函数性质，定义dp[l][r] 表示l,r 位置上包含了 r-l+1个0开始的连续排列
# dp[l][r]=max(dp[l+1][r],dp[l][r−1])+包含[l,r]的区间的个数 
# 然后 dp[l][r] 又引出了另一个问题， 已知N个区间标记[li,ri]表示区间被选中，求区间[lq,rq] 被多少个区间标记包含？ : algorithm/技巧/非连续值域变成连续值域处理/构造连续值域空间/构造查询连续空间/子问题.md




import init_setting
from lib.cflibs import *
def main(): 
    n, q = MII()
    cnt = [[0] * n for _ in range(n)]
    
    for _ in range(q):
        l, r = GMI()
        cnt[l][r] += 1
    
    for l in range(n):
        for r in range(n - 1, 0, -1):
            cnt[l][r - 1] += cnt[l][r]
    
    for l in range(1, n):
        for r in range(n):
            cnt[l][r] += cnt[l - 1][r]
    
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = cnt[i][i]
    
    for step in range(1, n):
        for l in range(n - step):
            r = l + step
            dp[l][r] = fmax(dp[l + 1][r], dp[l][r - 1]) + cnt[l][r]
    
    print(dp[0][n - 1])