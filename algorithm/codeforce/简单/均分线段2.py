# https://codeforces.com/gym/102409/problem/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1015/solution/cf102409j.md
# 如果不确定选前后哪个点，则保证选取切分点的前面小于后面，再考虑后面那个店的情况


import init_setting
from lib.cflibs import *
def main():
    n, l = MII()
    nums = [0] + LII() + [l]
    
    ans = l
    p1 = p2 = 0
    
    for i in range(2, n - 1):
        while nums[p1 + 1] <= nums[i] - nums[p1 + 1]:
            p1 += 1
        while nums[p2 + 1] - nums[i] <= l - nums[p2 + 1]:
            p2 += 1
        
        for d1 in range(p1, p1 + 2):
            for d2 in range(p2, p2 + 2):
                ma = max(nums[d1], nums[i] - nums[d1], nums[d2] - nums[i], l - nums[d2])
                mi = min(nums[d1], nums[i] - nums[d1], nums[d2] - nums[i], l - nums[d2])
                ans = fmin(ans, ma - mi)
    
    print(ans)