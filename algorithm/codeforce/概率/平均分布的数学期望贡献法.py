# https://codeforces.com/gym/102986/problem/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0328/solution/cf102986g.md
# algorithm/codeforce/docs/平均分布的时候数学期望贡献法绝对值展开.md
# 把前后两项的期望合并为w,中间部分由于有绝对值，并且是平均分布，所以用贡献法求当前值在所有期望和的贡献是有多少个是正，多少个事负

import init_setting
from cflibs import *
def main(): 
    n, w = MII()
    nums = LII()
    nums.sort()
    
    ans = 0
    for i in range(n):
        ans += (2 * i - (n - 1)) * nums[i]
    
    print(ans * 2 / n + w)