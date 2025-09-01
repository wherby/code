# https://codeforces.com/problemset/problem/490/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/04/0422/solution/cf490d.md
# 有两个变换一个是 /3 *2 一个是 /2， 使用最小变换，使得两个面积相等
# 因为 /3*2 会减少3的因数增加2的因数，所以优先选择
# 如果 3,2 因子都匹配完成，剩余不相等，则不能完成操作
from cflibs import *
def main():
    a1, b1 = MII()
    a2, b2 = MII()

    def c3(x):
        cnt = 0
        while x % 3 == 0:
            x //= 3
            cnt += 1
        return cnt

    def c2(x):
        cnt = 0
        while x % 2 == 0:
            x //= 2
            cnt += 1
        return cnt

    ans = 0

    v = c3(a1) + c3(b1) - c3(a2) - c3(b2)
    while v > 0:
        v -= 1
        ans += 1
        if a1 % 3 == 0: a1 = a1 // 3 * 2
        else: b1 = b1 // 3 * 2

    while v < 0:
        v += 1
        ans += 1
        if a2 % 3 == 0: a2 = a2 // 3 * 2
        else: b2 = b2 // 3 * 2

    v = c2(a1) + c2(b1) - c2(a2) - c2(b2)
    while v > 0:
        v -= 1
        ans += 1
        if a1 % 2 == 0: a1 = a1 // 2
        else: b1 = b1 // 2

    while v < 0:
        v += 1
        ans += 1
        if a2 % 2 == 0: a2 = a2 // 2
        else: b2 = b2 // 2

    if a1 * b1 == a2 * b2:
        print(ans)
        print(a1, b1)
        print(a2, b2)
    else: print(-1)