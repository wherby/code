# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0423/solution/cf106494d.md
# https://codeforces.com/gym/106494/problem/D
# 如果只有非负数，显然每个数放一组更优
# 如果有两个负数组，显然合并负数组更好
# 如果把负数组都合并，再加入正数的话，可以使得负数平均值往右移动，加入任何正数的效果一样，就越小越好，所以可以从小到大加入非负数，
# 这样就变成了从左到右遍历数组，统一操作，右边是独立数字，左边是当前维护的“负数组”





import init_setting
from cflibs import *
def main():
    n = II()
    nums = LII()
    nums.sort()
    
    total = 2 * sum(nums)
    ans = total
    
    for i in range(n):
        total -= 2 * nums[i]
        ans = fmax(ans, total + nums[i // 2] + nums[i - i // 2])
    
    print(ans)