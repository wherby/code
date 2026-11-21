# https://codeforces.com/gym/106806/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/11/1106/solution/cf106806e.md
# 如果循环节是1 的时候讨论
# 和查询是否有循环节

import init_setting
from lib.cflibs import *


def main():
    s = I()
    n = len(s)

    if min(s) == max(s):
        print(n)
        print(" ".join(s))
    else:
        for i in range(2, n):
            if n % i == 0:
                flg = True
                for j in range(n):
                    if s[j] != s[j % i]:
                        flg = False
                        break

                if flg:
                    print(2)
                    print(s[0], s[1:])
                    exit()

        print(1)
        print(s)
