# https://codeforces.com/problemset/problem/625/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0703/solution/cf625a.md

import sys
sys.path.append("..")
from cflibs.cflibs import *
def main():
    n = II()
    a = II()
    b = II()
    c = II()

    ans = 0
    if n >= b and b - c <= a:
        ans = (n - b) // (b - c) + 1
        n -= ans * (b - c)
    ans += n // a

    print(ans)