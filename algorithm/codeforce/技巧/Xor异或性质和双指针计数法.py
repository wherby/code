# https://codeforces.com/gym/105319/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/12/1220/solution/cf105319d.md
# 按位计算，累积影响
# 在双指针计算最长可以取上升路径的数组的时候，用 c0,c1记录对应最高需要修改的位数的累计数字，如果同一位冲突，则边界找到，再移动l的时候，同时也需要更新记录
# 寻求子数组元素异或X之后能成为非递减子数组的个数




import init_setting
from cflibs import *
def main(): 
    n = II()
    nums = LII()
    
    l, r = 0, 0
    ans = 0
    
    c0 = [0] * 30
    c1 = [0] * 30
    
    while l < n:
        while r + 1 < n:
            v = (nums[r] ^ nums[r + 1]).bit_length() - 1
            if v >= 0:
                if nums[r] >> v & 1:
                    if c0[v]: break
                    c1[v] += 1
                else:
                    if c1[v]: break
                    c0[v] += 1
            r += 1
        
        ans += r - l + 1
        if l + 1 < n:
            v = (nums[l] ^ nums[l + 1]).bit_length() - 1
            if v >= 0:
                if nums[l] >> v & 1: c1[v] -= 1
                else: c0[v] -= 1
        l += 1
    
    print(ans)