# https://codeforces.com/problemset/problem/593/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/04/0426/solution/cf593c.md
# 构造一个脉冲函数
import sys
sys.path.append("../..")

from cflibs import *
def main():
    n = II()

    xs = []
    ys = []

    for _ in range(n):
        x, y, r = MII()
        xs.append(x)
        ys.append(y)

    def solve(lst):
        print('(' * (n - 1), end='')
        for i in range(n):
            if i: print('+', end='')
            print(f'({lst[i] // 2}*((1-abs((t-{i})))+abs((1-abs((t-{i}))))))', end='')
            if i: print(')', end='')
        print()

    solve(xs)
    solve(ys)

main()

