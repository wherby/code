# https://codeforces.com/problemset/problem/207/B3
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0724/solution/cf207b3.md
# 从后到前利用倍增计算最多跳跃数量
# nums[i]记录在i 点所能向前跳跃的最小值
# 如果i点最多能跳跃到num[i], 但是要最优跳跃，从i跳跃的点应该是min(num[k] for k in range(nums[i],i+1))
# 从零阶最优来构建倍增最优
# [nums[i] * (2 * n) + i for i in range(2 * n)] 用于编码移动的距离nums[i]和选择的i
# 因为移动的步数是K,在k+1的时候才完成，所以最后要+2， 如果不用移动就可以达到，则需要特判+1

import init_setting
from cflibs import *
from lib.sparsetable import SparseTable
def main():
    n = II()
    
    nums = [II() for _ in range(n)]
    nums += nums
    
    for i in range(2 * n):
        nums[i] = fmax(0, i - nums[i])
    
    st = SparseTable([nums[i] * (2 * n) + i for i in range(2 * n)], fmin)
    
    nth_step = [[0] * (2 * n) for _ in range(20)]
    
    for i in range(2 * n):
        nth_step[0][i] = st.query(nums[i], i) % (2 * n)
    
    for i in range(19):
        for j in range(2 * n):
            nth_step[i + 1][j] = nth_step[i][nth_step[i][j]]
    
    ans = 0
    
    for i in range(n, 2 * n):
        if i - nums[i] >= n - 1:
            ans += 1
            continue
        
        cur = i
        for j in range(19, -1, -1):
            if i - nums[nth_step[j][cur]] < n - 1:
                ans += 1 << j
                cur = nth_step[j][cur]
        ans += 2
    
    print(ans)

#main()
# n = 4
# nums=[1,2,3,4]
# nums= nums+nums
# print([nums[i] * (2 * n) + i for i in range(2 * n)])