# https://codeforces.com/gym/106368/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/11/1120/solution/cf106368d.md
# 题目等同于在一个增长的stack中，维护一个堆排序
# 这里采用index的最低位作为排序区间进行了一个类似二进制堆排序的操作

import init_setting
from cflibs import *


def main():
    t = II()

    stk = []

    n = t // 2
    cur = 0
    timestamps = [0] * (n + 1)

    for i in range(1, t + 1):
        op, x = LI()
        x = int(x)

        ops = []

        if op == "+":
            cur += 1
            timestamps[cur] = x
        else:
            ops.append(f"2 {stk.pop()}")

        w = 2 * (i & -i) - 1
        tmp = [cur] if op == "+" else []

        while w and stk:
            w -= 1
            ops.append(f"2 {stk[-1]}")
            tmp.append(stk.pop())

        tmp.sort(lambda x: -timestamps[x])

        for x in tmp:
            ops.append(f"1 {x}")
            stk.append(x)

        print(len(ops))
        print("\n".join(ops), flush=True)
