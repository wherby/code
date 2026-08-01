# https://codeforces.com/gym/104670/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/07/0724/solution/cf104670a.md


import init_setting
from lib.cflibs import *
def main():
    n, c = MII()
    nums = LII()
    
    inf = 10 ** 9
    v1 = inf
    v2 = -inf
    
    ans = [0] * n
    
    for i in range(n):
        v1 = fmin(v1, nums[i] - i * c)
        v2 = fmax(v2, nums[i] + i * c)
        ans[i] = fmax((nums[i] - i * c) - v1, v2 - (nums[i] + i * c))
    
    print(' '.join(map(str, ans)))