# https://codeforces.com/gym/102129/problem/K
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0828/solution/cf102129k.md
# 以 a1,a2,a3 为例  a1 -(a2-a3) ,a1-a2-a3 => a1-a2 + a3,a1-a2-a3
# a1,a2,a3,a4 => a4也会同时出现 + ，- 号，且概率相等

import init_setting
from cflibs import *
def main():
    n = II()
    nums = LII()
    mod = 10 ** 9 + 7
    
    print((nums[0] - nums[1] + mod) % mod)