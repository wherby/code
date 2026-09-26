# https://codeforces.com/gym/106682/problem/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/09/0905/solution/cf106682e.md
# x+y = 2**k-1  虽然匹配是一个图，但是从大到小考虑，每个数字可能的匹配就可能是唯一的
# 这其实也是用最小信息描述连接区域的问题



import init_setting
from cflibs import *
def main():
    n = II()
    d = {}

    for _ in range(n):
        a, c = MII()
        d[a] = c


    for x in sorted(d, reverse=True):
        if d[x]:
            v = (1 << x.bit_length()) - 1 - x
            if v not in d or d[v] < d[x]:
                exit(print('Ana'))
            d[v] -= d[x]

    print('Beto')