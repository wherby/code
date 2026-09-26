# https://codeforces.com/gym/102760/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/08/0825/solution/cf102760d.md
# 两种贪心思维求最大最小化MST的边权标记
# 最小化就是用最小的边去标记关键边
# 最大化的时候，需要把最小的边去填子完全图，这样才能最大化MST


import init_setting
from cflibs import *
def main():
    n = II()
    nums = LII()
    
    nums.sort()
    
    mn = sum(nums[:n - 1])
    mx = 0
    
    for i in range(1, n):
        mx += nums[i * (i - 1) // 2]
    
    print(mn, mx)