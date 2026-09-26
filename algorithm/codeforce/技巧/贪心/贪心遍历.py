# https://codeforces.com/gym/106706/problem/M
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0917/solution/cf106706m.md
# 一定有一个切割点的时候，NEX是切割点
# 所以遍历所有切割点，得到左或右部分的，这时有可能改点相对左或者右部分的点不是MEX点，但是这里不重要，因为真正的切割点是满足这个条件的


import init_setting
from cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n = II()
        nums = LII()
        
        ans = n * (n - 1) // 2 - 1
        
        cur = 0
        for i in range(n):
            ans = fmax(ans, cur - nums[i])
            cur += nums[i]
        
        cur = 0
        for i in range(n - 1, -1, -1):
            ans = fmax(ans, cur - nums[i])
            cur += nums[i]
        
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))