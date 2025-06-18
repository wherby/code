# https://codeforces.com/problemset/problem/297/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/06/0614/solution/cf297c.md
# 这只是构造一个最大可能的方式，但是可能构造的数据不成功？？


import sys
sys.path.append("..")
from cflibs.cflibs import *
def main():
    n = II()
    nums = LII()

    order = sorted(range(n), key=lambda x: nums[x])

    k1 = (n + 2) // 3
    k2 = k1 * 2

    ans1 = [0] * n
    ans2 = [0] * n

    for i in range(k1):
        ans1[order[i]] = i
        ans2[order[i]] = nums[order[i]] - ans1[order[i]]

    for i in range(k1, k2):
        ans2[order[i]] = i
        ans1[order[i]] = nums[order[i]] - ans2[order[i]]

    for i in range(k2, n):
        ans2[order[i]] = n - 1 - i
        ans1[order[i]] = nums[order[i]] - ans2[order[i]]

    print('YES')
    print(' '.join(map(str, ans1)))
    print(' '.join(map(str, ans2)))