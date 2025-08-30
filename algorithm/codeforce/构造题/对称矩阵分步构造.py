# https://codeforces.com/problemset/problem/201/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0829/solution/cf201a.md
# 无领边的对称图形最多能放多少个
# 如果是偶数，则满足对称且无领边必然比奇数少
# 计算奇数的时候排列，可以最多达到空位的一半取上整个

import init_setting
from cflibs import *
def main():
    x = II()
    if x == 3: exit(print(5))
    for n in range(1, 101, 2):
        if n * n + 1 >= 2 * x:
            print(n)
            break