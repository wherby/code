# https://codeforces.com/problemset/problem/373/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/05/0524/solution/cf373b.md
# 这里求剩余数字用 v-m ,在有剩余的时候添加到m中实现下限进位操作


import init_setting
from cflibs import *
def main():
    w, m, k = MII()

    w //= k

    v = 10
    digit = 1

    ans = 0

    while True:
        l = fmax(0, v - m)
        if l * digit <= w:
            w -= l * digit
            ans += l
            m += l
        else:
            ans += w // digit
            break
        
        v *= 10
        digit += 1

    print(ans)