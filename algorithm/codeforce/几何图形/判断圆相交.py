# https://codeforces.com/problemset/problem/199/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0707/solution/cf199b.md
# 判断一个圆与其他两个同心圆是否相交，在小同心圆外。在大同心圆内，和在两圆之间
# 如果两个圆的圆心距离小于两个圆的半径差，则小圆一定在大圆内 【内离】
# 如果两个圆的半径差大于两个圆心距离，则两个圆必定不相交 【外离】


import init_setting
from lib.cflibs import *
def main():
    x1, y1, r1, R1 = MII()
    x2, y2, r2, R2 = MII()

    v = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)

    def check(f, r0, r, R):
        if r >= r0 and (r - r0) * (r - r0) >= f: return 1
        if R <= r0 and (R - r0) * (R - r0) >= f: return 1
        if (R + r0) * (R + r0) <= f: return 1
        return 0

    print(check(v, r1, r2, R2) + 
        check(v, R1, r2, R2) + 
        check(v, r2, r1, R1) + 
        check(v, R2, r1, R1))