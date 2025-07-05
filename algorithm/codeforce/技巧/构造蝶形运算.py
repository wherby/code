# https://codeforces.com/problemset/problem/234/G
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0704/solution/cf234g.md
# 原题是N个元素，分组使得两两在不同组的最小分组方式，和FFT的蝶形运算类似

import sys
sys.path.append("..")
from cflibs.cflibs import *
def main():
    fin = open('input.txt', 'r')
    fout = open('output.txt', 'w')

    input = lambda: fin.readline().strip()

    def fprint(x):
        fout.write(str(x))
        fout.write('\n')

    n = II()
    k = (n - 1).bit_length()

    fprint(k)

    for i in range(k):
        tmp = [j for j in range(n) if j >> i & 1]
        fprint(f"{len(tmp)} {' '.join(map(str, tmp))}")