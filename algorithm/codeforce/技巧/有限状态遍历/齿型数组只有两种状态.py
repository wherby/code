# https://codeforces.com/gym/105934/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/11/1105/solution/cf105934c.md
# 要构成齿型数组，每个位置只有两种状态，波峰和波谷，
# 对当前值修改是最大的优势(可以减少下一个位置的操作次数)，贪心求解下一状态



import init_setting
from cflibs import *
def main(): 
    n = II()
    nums = LII()
    
    ans = 10 ** 16
    
    res = 0
    cur = nums[0]
    
    for i in range(1, n):
        if i % 2:
            cur = fmax(cur + 1, nums[i])
            res += cur - nums[i]
        else:
            cur = fmin(cur - 1, nums[i])
            res += nums[i] - cur
    
    ans = fmin(ans, res)
    
    res = 0
    cur = nums[0]
    
    for i in range(1, n):
        if i % 2 == 0:
            cur = fmax(cur + 1, nums[i])
            res += cur - nums[i]
        else:
            cur = fmin(cur - 1, nums[i])
            res += nums[i] - cur
    
    ans = fmin(ans, res)
    
    print(ans)