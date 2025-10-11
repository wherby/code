# https://codeforces.com/gym/104380/problem/F
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1010/solution/cf104380f.md
# 讨论哪些点不能进入选择

import init_setting
from lib.cflibs import *
def main():
    n, l, r = MII()
    nums = LII()
    
    v = fmin(l - 1, n - r)
    nums = nums[:n - v]
    print(sum(nlargest(r - l + 1, nums)))