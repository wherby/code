# https://codeforces.com/gym/106494/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0422/solution/cf106494c.md
# 分情况考虑：
# 如果非负数数量大于负数数量，则所有负数都能被非负数消除
# 如果非负数数量小于负数数量，则用非负数匹配消除对称位的负数，则最后会留下一个只有负数的子序列
# 两种情况都可以先保留非负数，第二种情况下负数序列的中位数正好也是 nums[n // 2]， 第一种情况不存在负数子序列


import init_setting
from cflibs import *
def main():
    n = II()
    nums = LII()
    nums.sort()
    print(sum(fmax(0, x) for x in nums) + fmin(nums[n // 2], 0))