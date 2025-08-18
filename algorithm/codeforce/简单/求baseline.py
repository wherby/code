# https://codeforces.com/problemset/problem/67/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/08/0818/solution/cf67a.md
# 双向约束，用两个方向的遍历解决
# algorithm/codeforce/简单/test/testArrayBaseline.py 用另一种方式解决？ 这样写是错误的，因为L的时候，右边不一定只能减少1，有可能减少更大也可以满足，所以需要从右到左用最小增加法处理

import init_setting
from lib.cflibs import *
def main():
    n = II()
    s = I()
    
    ans = [1] * n
    
    for i in range(n - 1):
        if s[i] == 'R': ans[i + 1] = ans[i] + 1
        elif s[i] == '=': ans[i + 1] = ans[i]
    
    for i in range(n - 2, -1, -1):
        if s[i] == 'L': ans[i] = fmax(ans[i], ans[i + 1] + 1)
        elif s[i] == '=': ans[i] = ans[i + 1]
    
    print(*ans)
main()

# 7
# =RRRLL