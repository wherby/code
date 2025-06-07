# https://codeforces.com/problemset/problem/266/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/06/0605/solution/cf266c.md
# 要把1都移动到对角线下，则可以递归解决问题
import sys
sys.path.append("..")
from cflibs.cflibs import *
def main():
    n = II()
    xs = []
    ys = []

    for _ in range(n - 1):
        x, y = GMI()
        xs.append(x)
        ys.append(y)

    outs = []

    for i in range(n, 1, -1):
        cnt_r = [0] * i
        cnt_c = [0] * i
        
        for j in range(n - 1):
            if xs[j] < i and ys[j] < i:
                cnt_r[xs[j]] += 1
                cnt_c[ys[j]] += 1
        
        for j in range(i - 1):
            if cnt_c[j] == 0:
                outs.append(f'2 {j + 1} {i}')
                for idx in range(n - 1):
                    if ys[idx] == i - 1:
                        ys[idx] = j
                break
        
        for j in range(i - 1):
            if cnt_r[j]:
                outs.append(f'1 {j + 1} {i}')
                for idx in range(n - 1):
                    if xs[idx] == j: xs[idx] = i - 1
                    elif xs[idx] == i - 1: xs[idx] = j
                break

    print(len(outs))
    print('\n'.join(outs))