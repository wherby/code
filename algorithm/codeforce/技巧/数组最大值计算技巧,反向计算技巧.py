# https://codeforces.com/gym/106043/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0926/solution/cf106043c.md
# 最大元素可以影响的范围就能构成所有范围内子数字形的最大值
# 要求最小的缺少元素，转换成每个小于当前元素能影响的最大长度的最小值
# 当这个最小值长度不是0，则表示在这个长度内的子数字，数字都有值
# 所以从大到小，更新值

import init_setting
from cflibs import *
def main():
    n = II()
    nums = LII()
    
    left = [0] * n
    right = [0] * n
    
    stk = [-1]
    
    for i in range(n):
        while stk[-1] != -1 and nums[stk[-1]] <= nums[i]:
            stk.pop()
        
        left[i] = stk[-1]
        stk.append(i)
    
    stk = [n]
    for i in range(n - 1, -1, -1):
        while stk[-1] != n and nums[stk[-1]] <= nums[i]:
            stk.pop()
        right[i] = stk[-1]
        stk.append(i)
    
    max_length = [0] * (n + 1)
    
    for i in range(n):
        if nums[i] < n:
            max_length[nums[i]] = fmax(max_length[nums[i]], right[i] - left[i] - 1)
    
    for i in range(1, n + 1):
        max_length[i] = fmin(max_length[i], max_length[i - 1])
    
    ans = [0] * (n + 1)
    
    for i in range(n + 1):
        ans[max_length[i]] = i + 1
    
    for i in range(n - 1, -1, -1):
        ans[i] = fmax(ans[i], ans[i + 1])
    
    print(' '.join(map(str, ans[1:])))