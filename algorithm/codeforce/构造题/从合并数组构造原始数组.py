# https://codeforces.com/problemset/problem/1906/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0722/solution/cf1906e.md
# 合并后的数列分离的时候，第一个数字为比较值，一直到比它大的数字都属于同一子数组，这些子数组会构成一个长度为N的数列，相邻的子数组不一定属于不同的数列，所以这里可以用背包DP
# 根据DP的值，从后到前分配数字 


import init_setting
from lib.cflibs import *
def main():
    n = II()
    nums = LII()
    
    intervals = []
    
    l = 0
    
    while l < n * 2:
        r = l
        while r + 1 < n * 2 and nums[r + 1] < nums[l]:
            r += 1
        intervals.append((l, r))
        l = r + 1
    
    dp = [-2] * (n + 1)
    dp[0] = -1
    
    for i in range(len(intervals)):
        x = intervals[i][1] - intervals[i][0] + 1
        for y in range(n, x - 1, -1):
            if dp[y - x] != -2 and dp[y] == -2:
                dp[y] = i
                print(dp,x,y)
    
    if dp[n] == -2:
        exit(print(-1))
    
    choice = [0] * (2 * n)
    cur = n
    print(dp,intervals)
    while cur:
        idx = dp[cur]
        l, r = intervals[idx]
        
        for i in range(l, r + 1):
            choice[i] = 1
        
        cur -= r - l + 1
    
    print(' '.join(str(nums[i]) for i in range(2 * n) if choice[i]))
    print(' '.join(str(nums[i]) for i in range(2 * n) if not choice[i]))

main()