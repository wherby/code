# https://codeforces.com/gym/102860/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/06/0605/solution/cf102860b.md
# 使用双指针求钝角三角形的个数


import init_setting
from lib.cflibs import *
def main():
    n, l = MII()
    nums = LII()
    nums.sort()
    
    for i in range(n):
        nums.append(nums[i] + l)
    
    ans = n * (n - 1) * (n - 2) // 6
    r = 0
    
    for i in range(n):
        while 2 * (nums[r] - nums[i]) < l:
            r += 1
        
        v = r - i - 1
        ans -= v * (v - 1) // 2
    
    print(ans)