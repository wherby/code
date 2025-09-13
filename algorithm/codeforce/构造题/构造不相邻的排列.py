# https://codeforces.com/problemset/problem/81/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0903/solution/cf81d.md
# 选取不相邻的排列，必然每类小于n//2，然后按照奇偶分别排列

import init_setting
from lib.cflibs import *
def main():
    n, m = MII()
    nums = LII()
    
    for i in range(m):
        nums[i] = fmin(nums[i], n // 2)
    
    total = []
    
    for i in sorted(range(m), key=lambda x: -nums[x]):
        while len(total) < n and nums[i]:
            total.append(i + 1)
            nums[i] -= 1
    
    if len(total) < n:
        exit(print(-1))
    
    ans = [0] * n
    
    pt = 0
    for x in total:
        ans[pt] = x
        pt += 2
        
        if pt >= n:
            pt = 1
    
    print(*ans)