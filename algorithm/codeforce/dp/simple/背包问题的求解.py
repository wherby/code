# https://codeforces.com/gym/102319/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/10/1009/solution/cf102319a.md
# 这里需要假设一个物品进行背包DP，所以直接求物品价值需要的容量，不需要从头递推


import init_setting
from cflibs import *
def main():
    n = II()
    l, r = MII()
    nums = LII()
    
    inf = 10 ** 9
    
    dp = [inf] * (r + 1)
    dp[0] = 0
    
    for x in nums:
        for y in range(x, r + 1):
            dp[y] = fmin(dp[y], dp[y - x] + 1)
    
    cur_ans = sum(dp[l:r + 1])
    choice = 0
    
    for i in range(2, r + 1):
        new_ans = 0
        
        for x in range(l, r + 1):
            v = dp[x]
            for y in range(1, x // i + 1):
                v = fmin(v, dp[x - y * i] + y)
            new_ans += v
        
        if new_ans < cur_ans:
            cur_ans = new_ans
            choice = i
    
    print(choice)