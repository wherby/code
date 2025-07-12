# https://codeforces.com/problemset/problem/690/D2
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0708/solution/cf690d2.md
# 如果是小于C个物品 分到 N个目录下面，
# 只用物品的视角，则不好划分
# 把物品和目录都排序，则为N+C个物品，排列为1,2,.. N+C, 因为C个物品可以不分配完，所有我们选择10个数字作为划分的标记，就是C(N+C，N)
# 比如 1,2,4，。。N+X 表示第一个位置为空， 第二个位置也为空，第3个位置为1，最后有 C-X个物品没有分配


import sys
sys.path.append("..")
from cflibs.cflibs import *

def main():
    mod = 10 ** 6 + 3

    n, c = MII()
    v1 = 1
    v2 = 1

    for i in range(1, n + 1):
        v1 = v1 * (n + c + 1 - i) % mod
        v2 = v2 * i % mod

    print((v1 * pow(v2, -1, mod) % mod - 1) % mod)