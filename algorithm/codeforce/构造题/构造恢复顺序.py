# https://codeforces.com/problemset/problem/534/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/06/0609/solution/cf534d.md
# 不可能的情况判断？

import sys
sys.path.append("..")
from cflibs.cflibs import *
def main():
    n = II()
    nums = LII()

    tmp = [[] for _ in range(n + 4)]
    for i in range(n):
        tmp[nums[i]].append(i)

    cur = 0
    ans = []

    for _ in range(n):
        while True:
            if tmp[cur]:
                ans.append(tmp[cur].pop())
                break
            else:
                if cur < 3: exit(print('Impossible'))
                cur -= 3
        cur += 1

    print('Possible')
    print(' '.join(str(x + 1) for x in ans))