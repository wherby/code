# https://codeforces.com/gym/104523/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0224/solution/cf104523d.md
# 计算损失函数的时候，3是最优解，所以长度都会以2，或者3为单位增加
# 消去DP的时候设置边界为0 
# 因为是消去之后的DP，所以首先求取区间是否能完整消去，使用剥洋葱的方式计算，如果是2的长度，则用首位比较，如果是3的长度，则用首位和遍历中位比较
# 然后利用得到的DP值，使用DP求解最短值和最小cost
# algorithm/codeforce/dp/docs/DP求最佳结果和cost.md 拉式DP的写法


import init_setting
from cflibs import *
def main(): 
    t = II()
    outs = []
    
    inf = 10 ** 9
    
    for _ in range(t):
        n, k = MII()
        nums = LII()
        
        dp = [[inf] * n for _ in range(n)]
        
        for i in range(1, n):
            dp[i][i - 1] = 0
        
        for diff in range(1, n):
            for l in range(n - diff):
                r = l + diff
                for i in range(l, r):
                    dp[l][r] = fmin(dp[l][r], dp[l][i] + dp[i + 1][r])
                
                ma = fmax(nums[l], nums[r])
                mi = fmin(nums[l], nums[r])
                
                for i in range(l + 1, r):
                    if fmax(ma, nums[i]) - fmin(mi, nums[i]) <= k:
                        dp[l][r] = fmin(dp[l][r], dp[l + 1][i - 1] + dp[i + 1][r - 1] + 1)
                
                if ma - mi <= k:
                    dp[l][r] = fmin(dp[l][r], dp[l + 1][r - 1] + 1)
        
        dp1 = [inf] * (n + 1)
        dp2 = [inf] * (n + 1)
        
        dp1[0] = 0
        dp2[0] = 0
        
        for i in range(n):
            if dp1[i + 1] > dp1[i] + 1 or (dp1[i + 1] == dp1[i] + 1 and dp2[i + 1] > dp2[i]):
                dp1[i + 1] = dp1[i] + 1
                dp2[i + 1] = dp2[i]
            
            for j in range(i, n):
                if dp[i][j] < inf:
                    if dp1[j + 1] > dp1[i] or (dp1[j + 1] == dp1[i] and dp2[j + 1] > dp2[i] + dp[i][j]):
                        dp1[j + 1] = dp1[i]
                        dp2[j + 1] = dp2[i] + dp[i][j]
        
        outs.append(f'{dp1[n]} {dp2[n]}')
    
    print('\n'.join(outs))