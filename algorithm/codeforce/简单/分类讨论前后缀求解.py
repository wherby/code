# https://codeforces.com/gym/106042/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0926/solution/cf106042d.md
# 对每个位置分情况讨论，用前后缀计算各个情况分布

import init_setting
from lib.cflibs import *
def main():
    t = II()
    outs = []
    
    for _ in range(t):
        n, x, y = MII()
        nums = LII()
        
        tmp = [v - (v & y) for v in nums]
        
        pref_min = [2 * 10 ** 9] * (n + 1)
        for i in range(n):
            pref_min[i + 1] = fmin(pref_min[i], tmp[i])
        
        suff_min = [2 * 10 ** 9] * (n + 1)
        for i in range(n - 1, -1, -1):
            suff_min[i] = fmin(suff_min[i + 1], tmp[i])
    
        total = sum(nums)
        ans = 10 ** 15
        
        for i in range(n):
            res = total - nums[i] + (nums[i] | x)
            to_delete = fmin(pref_min[i], suff_min[i + 1])
            to_delete = fmin(to_delete, (nums[i] | x) - ((nums[i] | x) & y))
            res -= to_delete
            ans = fmin(ans, res)
        
        outs.append(ans)
    
    print('\n'.join(map(str, outs)))