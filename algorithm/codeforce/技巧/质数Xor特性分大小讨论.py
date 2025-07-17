# https://codeforces.com/problemset/problem/1991/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0715/solution/cf1991d.md
# 除了2 之外，所有质数都是奇数 
# 当 N 小于6 的时候，题目已知需要 n//2 +1 个种类
# 当 N 大于6时候：
# 如果奇数，偶数分成两个颜色，需要同时考虑两个相邻的数字异或为2，则需要分为4个类型

import init_setting
from cflibs import *
def main():
    t = II()
    outs = []

    for _ in range(t):
        n = II()
        if n <= 5:
            outs.append(str(n // 2 + 1))
            outs.append(' '.join(str(x // 2 + 1) for x in range(1, n + 1)))
        else:
            outs.append('4')
            outs.append(' '.join(str(x % 4 + 1) for x in range(n)))

    print('\n'.join(outs))