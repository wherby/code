# https://codeforces.com/problemset/problem/471/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0730/solution/cf471c.md
# 这里有两个问题，第一是最少card搭建N层的求和数列计算，第二是可以被搭建的层数基于3的是同余数列


import init_setting
from cflibs import *
def main():
    n = II()
    
    l, r = 1, 10 ** 9
    while l <= r:
        mid = (l + r) // 2
        if mid * (3 * mid + 1) // 2 <= n:
            l = mid + 1
        else:
            r = mid - 1
    
    print((r - (3 - n % 3)) // 3 + 1)