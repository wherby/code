# https://codeforces.com/problemset/problem/741/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/06/0628/solution/cf741a.md
# 判定图上所有的点都在环上

import init_setting
from cflibs import *


def main():
    n = II()
    perm = LGMI()

    vis = [0] * n
    ans = 1

    for i in range(n):
        if not vis[i]:
            x = i
            c = 0
            while not vis[x]:
                vis[x] = 1
                x = perm[x]
                c += 1
            
            if x != i:
                exit(print(-1))
            
            if c % 2 == 0: c //= 2
            ans = math.lcm(ans, c)

    print(ans)