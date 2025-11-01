# https://codeforces.com/gym/104599/problem/I
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/10/1029/solution/cf104599i.md
# 叶子到根方向DP,有两个叶子节点的连接和，叶子到当前节点的连接两种方式
# dp1,dp2维护两个最长的子路径距离


import init_setting
from lib.cflibs import *
def main(): 
    n = II()
    nums = LII()
    parent = [-1] + LGMI()
    
    ans = 0
    dp1 = [0] * n
    dp2 = [0] * n
    
    for i in range(n - 1, -1, -1):
        ans = fmax(ans, dp1[i] + dp2[i])
        ans = fmax(ans, nums[i] + dp1[i])
        
        if i > 0:
            v = fmax(nums[i], dp1[i]) + 1
            p = parent[i]
            if v > dp1[p]: dp1[p], dp2[p] = v, dp1[p]
            elif v > dp2[p]: dp2[p] = v
    
    print(ans)