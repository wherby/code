# https://codeforces.com/problemset/problem/508/E
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0704/solution/cf508e.md
# 贪心维护两个位置，cur是绝对位置，为括号idx,val是右括号的相对位置
# 用dfs维护相对位置的距离，用cur维护当前已经处理了多少个左端点
# 用 i 记录当前循环里的绝对位置idx，

import init_setting
from cflibs import *
def main():
    n = II()
    ls = []
    rs = []

    for _ in range(n):
        l, r = MII()
        ls.append(l)
        rs.append(r)

    cur = -1
    ans = []

    def dfs(i):
        nonlocal cur
        ans.append('(')
        
        val = 1
        while val < ls[i] and cur + 1 < n:
            cur += 1
            val += dfs(cur)
        
        if not ls[i] <= val <= rs[i]:
            exit(print('IMPOSSIBLE'))
        
        ans.append(')')
        return val + 1

    while cur + 1 < n:
        cur += 1
        dfs(cur)

    print(''.join(ans))