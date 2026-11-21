# https://codeforces.com/gym/106611/problem/L
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/11/1110/solution/cf106611l.md
# 标记 s[u] = -3 和 -2  不仅是表示类型不同，还能满足后续操作中total ！=0的要求

import init_setting
from cflibs import *


def main():
    n = II()
    s = [int(c) if c != "?" else -1 for c in I()]

    ans = 0
    stk = [i for i in range(n) if s[i] != -1]

    while stk:
        x = stk.pop()

        if s[x] >= 0:
            total = s[x]
            tmp = []

            for dx in [-1, 1]:
                if 0 <= x + dx < n:
                    if s[x + dx] == -1:
                        tmp.append(x + dx)
                    elif s[x + dx] == -2:
                        total -= 1

            if total == 0:
                for u in tmp:
                    ans += 1
                    s[u] = -3
                    stk.append(u)

            elif total == len(tmp):
                for u in tmp:
                    s[u] = -2
                    stk.append(u)
        else:
            saved_x = x
            for vx in [-1, 1]:
                x = saved_x + vx
                if 0 <= x < n:
                    total = s[x]
                    tmp = []

                    for dx in [-1, 1]:
                        if 0 <= x + dx < n:
                            if s[x + dx] == -1:
                                tmp.append(x + dx)
                            elif s[x + dx] == -2:
                                total -= 1

                    if total == 0:
                        for u in tmp:
                            ans += 1
                            s[u] = -3
                            stk.append(u)
                    elif total == len(tmp):
                        for u in tmp:
                            s[u] = -2
                            stk.append(u)

    print(ans)
