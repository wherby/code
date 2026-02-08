# https://codeforces.com/gym/104758/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/02/0202/solution/cf104758d.md
# 使用前后缀最大值确定当前贡献值，如果当前值为0，则状态清零
# 也可以使用单调栈维护前后缀最大值，计算贡献值。




import init_setting
from cflibs import *

def main(): 
    n = II()
    nums = LII()
    
    pref = nums[:]
    for i in range(1, n):
        pref[i] = fmax(pref[i - 1], pref[i])
    
    suff = nums[:]
    for i in range(n - 2, -1, -1):
        suff[i] = fmax(suff[i], suff[i + 1])
    
    ans = 0
    cur = 0
    
    for i in range(n):
        x = fmin(pref[i], suff[i]) - nums[i]
        if x == 0:
            cur = 0
        else:
            cur += x
        
        ans = fmax(ans, cur)
    
    print(ans)