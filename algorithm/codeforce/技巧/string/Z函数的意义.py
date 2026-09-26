# https://codeforces.com/gym/106644/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0817/solution/cf106644d.md
# 如果 z[i] == n - i， 则表示整个字符串是i为周期的循环字符串，有可能循环节不完整 

import init_setting
from cflibs import *
from lib.zfunction import z_algorithm
def main():
    n = II()
    nums = LII()
    
    z = z_algorithm(nums)
    
    outs = []
    cur = -1
    
    for i in range(1, n):
        if z[i] != n - i:
            cur = i
        outs.append(cur)
    
    print(' '.join(map(str, outs)))