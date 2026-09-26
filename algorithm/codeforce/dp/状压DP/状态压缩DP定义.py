# https://codeforces.com/gym/106682/problem/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0903/solution/cf106682c.md
# 状态与决策，从后到前看就是状态压缩DP


import init_setting
from cflibs import *
def main():
    n = II()
    v1 = [0] + LII()
    v2 = [0] + LII()

    w1, w2 = v1[n], v2[n]

    for i in range(n - 1, -1, -1):
        w1, w2 = fmax(w1, fmin(v1[i], w2)), fmin(w2, fmax(v2[i], w1))

    print(w1)