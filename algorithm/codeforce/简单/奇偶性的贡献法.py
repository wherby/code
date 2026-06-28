# https://codeforces.com/gym/106020/problem/M
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0627/solution/cf106020m.md
# 奇偶性与贡献法

import init_setting
from lib.cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        nums = LII()
        outs.append(sum(nums) ^ sum(nums[1:]) ^ sum(nums[:-1]) ^ sum(nums[1:-1]))
    
    print('\n'.join(map(str, outs)))