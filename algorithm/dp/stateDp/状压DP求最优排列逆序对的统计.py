# https://codeforces.com/gym/106500/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0427/solution/cf106500f.md
# 题目中状态数量比较少，在统计逆序对的时候，使用pairs[i][x] 表示累积有了多少个由数字i形成的逆序对(如果需要x在i左边的话形成的逆序对)
# 使用状态压缩DP，用状态表示已经排序好的最右边的数字，枚举下一个数字如果放置在这些数字最左边的时候需要处理的逆序对  (这里把新数字放左边或者右边就需要改pair的定义，最终的结果是对称的，两种做法都可以)


import init_setting
from cflibs import *
def main():
    n = II()
    nums = LGMI()
    
    cnt = [0] * 10
    pairs = [[0] * 10 for _ in range(10)]
    
    for x in nums:
        for i in range(10):
            pairs[i][x] += cnt[i]
        cnt[x] += 1
    
    inf = 10 ** 14
    
    dp = [inf] * (1 << 10)
    dp[0] = 0
    
    for i in range(1 << 10):
        for j in range(10):
            if i >> j & 1: continue
            
            ni = i | (1 << j)
            new_rev = 0
            
            for k in range(10):
                if i >> k & 1:
                    new_rev += pairs[k][j]
            
            dp[ni] = fmin(dp[ni], dp[i] + new_rev)
    
    print(dp[-1])