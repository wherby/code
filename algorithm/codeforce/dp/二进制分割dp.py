# https://codeforces.com/problemset/problem/757/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/03/0329/solution/cf757d.md
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/03/0329/personal_submission/cf757d_yawn_sean.py
# dp[x][y] x表示未分割的状态， y表示数字出现的status
# 因为前面一部分不算，所有每个位置都可以 dp[0][0] += 1


import sys
sys.path.append("..")
from cflibs.cflibs import *
# Submission link: https://codeforces.com/problemset/submission/757/312871611
def main():
    n = II()
    s = [int(c) for c in I()]

    total = 1 << 20

    dp = [[0] * total for _ in range(11)]
    dp_sep = [0] * total

    ans = 0
    mod = 10 ** 9 + 7

    possible = [0] * 11
    npossible = [0] * 11

    possible[0] = 1

    for i in range(n):
        dp[0][0] += 1
        if dp[0][0] >= mod:
            dp[0][0] -= mod
        
        possible[0] = 1
        
        # 做分割的时候，先把状态转移到dp_sep里保存下来
        for x in range(11):
            if not possible[x]: continue
            
            for y in range(total):
                if dp[x][y] and 1 <= x * 2 + s[i] <= 20:
                    ny = y | (1 << (x * 2 + s[i] - 1))
                    dp_sep[ny] += dp[x][y]
                    if dp_sep[ny] >= mod:
                        dp_sep[ny] -= mod

        for x in range(1, 20):
            ans += dp_sep[(1 << x) - 1]
            if ans >= mod: ans -= mod
        
        # 不做分割的时候的转移
        # 因为已经把不做分割的时候转移了，
        # 所有要把原来的状态清零，但是0这个状态累计不能更改，因为非零的状态都已经转移了
        for x in range(10, -1, -1):
            if possible[x]:
                if 2 * x + s[i] <= 10:
                    npossible[2 * x + s[i]] = 1
                    for y in range(total):
                        dp[2 * x + s[i]][y] = dp[x][y]
                if x + s[i]:
                    for y in range(total):
                        dp[x][y] = 0
        # 把转移的状态加回下一个状态
        for x in range(total):
            dp[0][x] += dp_sep[x]
            if dp[0][x] >= mod:
                dp[0][x] -= mod
            dp_sep[x] = 0
        
        # 这里是对尾数积累的转移
        for x in range(11):
            possible[x] = npossible[x]
            npossible[x] = 0

    print(ans)