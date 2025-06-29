# https://codeforces.com/problemset/problem/286/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/06/0627/solution/cf286b.md

import sys
sys.path.append("..")
from cflibs.cflibs import *
def main():
    n = II()
    ans = [0] * (2 * n)

    for i in range(n):
        ans[i] = i + 1

    for i in range(n):
        cur = 0
        for j in range(0, n, i + 1):
            ans[i + j], cur = cur, ans[i + j]
        ans[i + n] = cur

    print(' '.join(map(str, ans[n:])))