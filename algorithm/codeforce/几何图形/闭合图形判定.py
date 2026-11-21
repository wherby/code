# https://codeforces.com/gym/106806/problem/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/11/1105/solution/cf106806d.md
# 其实是图内有环的判定，如果把后面的圆心放前面的圆周上，可以解决后面的问题，但是最前面的圆心要放在其他圆周上，这时就需要找到一个集合能满足构成闭合图形的条件

import init_setting
from lib.cflibs import *


def main():
    n = II()
    nums = LII()

    nums.sort()

    cur = 0
    flg = False

    for x in nums:
        if cur >= x:
            flg = True
        cur += x

    print("possible" if flg else "impossible")
