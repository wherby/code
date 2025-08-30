# https://codeforces.com/problemset/problem/160/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0820/solution/cf160c.md
# 有相同数字的pair 排序的时候，相同首位的数字排序是交叉倍增的，所以这里用j-i表示相同首位的个数，而末尾就除以相同的倍数得到。



import init_setting
from lib.cflibs import *
def main():
    n, k = MII()
    nums = LII()
    nums.sort()
    
    k -= 1
    
    i = 0
    while i < n:
        j = i
        while j < n and nums[i] == nums[j]:
            j += 1
        
        if (j - i) * n > k:
            break
        
        k -= (j - i) * n
        i = j
    
    print(nums[i], nums[k // (j - i)])