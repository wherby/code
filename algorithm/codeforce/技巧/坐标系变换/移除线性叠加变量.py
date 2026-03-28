# https://codeforces.com/gym/105925/problem/J
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/03/0319/solution/cf105925j.md
# 因为K>0所以最多可以跑一圈，运动在没个位置都会增加k，可以使得线性叠加变量减去，变成了单调栈解决找到比当前小的下一个位置即可

import init_setting
from cflibs import *
def main(): 
    n, k = MII()
    nums = LII()
    
    for i in range(n):
        nums.append(nums[i])
    
    for i in range(2 * n):
        nums[i] -= i * k
    
    ans = [0] * n
    
    stk = []
    for i in range(2 * n - 1, -1, -1):
        while stk and nums[stk[-1]] >= nums[i]:
            stk.pop()
        if i < n: ans[i] = stk[-1] % n + 1
        stk.append(i)
    
    print(' '.join(map(str, ans)))