# https://codeforces.com/gym/101875/problem/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/09/0911/solution/cf101875a.md
# 在环形的图里，gcd 决定了最大值对的时候，步长是多少，而一个区间里步长里的其他点可以用k-1步长遍历。


import init_setting
from lib.cflibs import *
def main():
    n, k = MII()
    g = math.gcd(n, k)
    print((n - g) * k + (g - 1) * (k - 1))