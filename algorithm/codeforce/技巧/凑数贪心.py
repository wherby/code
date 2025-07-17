# https://codeforces.com/problemset/problem/313/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0705/solution/cf313e.md
# 两个数字加上等于 m-1 有两种情况，大于m-1 和小于等于m-1
# 通过stack 存了所有可能小于等于m-1的candidate， 如果stack里面不为空， 则是大于m-1的组合，则大大配对就是最大的组合


import init_setting
from cflibs import *
def main():
    n, m = MII()
    nums1 = LII()
    nums2 = LII()

    c1 = [0] * m
    c2 = [0] * m

    for x in nums1: c1[x] += 1
    for x in nums2: c2[x] += 1

    ans = []
    stk = []

    for i in range(m):
        stk.extend(i for _ in range(c1[i]))
        
        while c2[m - i - 1] and stk:
            c2[m - i - 1] -= 1
            ans.append(stk.pop() + m - i - 1)

    for i in range(m - 1, -1, -1):
        while c2[i]:
            c2[i] -= 1
            ans.append(stk.pop() + i - m)

    ans.sort(reverse=True)

    print(' '.join(map(str, ans)))