# https://codeforces.com/problemset/problem/435/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/05/0531/solution/cf435c.md

import init_setting
from cflibs import *
def main():
    n = II()
    nums = [0] + LII()
    total = sum(nums)

    for i in range(1, n + 1):
        if i % 2: nums[i] = nums[i - 1] - nums[i]
        else: nums[i] = nums[i - 1] + nums[i]

    mi = min(nums)
    ma = max(nums)

    for i in range(n + 1):
        nums[i] -= mi

    ans = [[' '] * total for _ in range(ma - mi)]

    cur = 0
    for i in range(n):
        l, r = nums[i], nums[i + 1]
        if l < r:
            for j in range(nums[i + 1] - nums[i]):
                ans[nums[i] + j][cur + j] = '\\'
            cur += r - l
        else:
            for j in range(nums[i] - nums[i + 1]):
                ans[nums[i] - 1 - j][cur + j] = '/'
            cur += l - r

    print('\n'.join(''.join(x) for x in ans))