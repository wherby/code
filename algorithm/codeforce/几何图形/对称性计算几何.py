# https://codeforces.com/gym/106797/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/11/1105/solution/cf106797e.md
# 这里选46度，其实是利用了“对称性质”，无论起点在哪个角度，都可以在一个区间内匹配？
# 题解里给出的是另一个解法，利用三角形的全等，可以得知当前三角形的高等于原正方形的边长一半


import init_setting
from lib.cflibs import *


def main():
    t = II()

    for _ in range(t):
        print("? 1 0", flush=True)
        d1 = float(I())
        print("? 1 1", flush=True)
        d2 = float(I())

        d = math.sqrt(d1 * d1 + d2 * d2 - d1 * d2 * math.sqrt(2))
        h = d1 * d2 * math.sqrt(2) / 2 / d
        print(f"! {round(4 * h * h)}", flush=True)
