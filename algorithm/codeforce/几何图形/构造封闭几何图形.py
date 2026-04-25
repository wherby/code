# https://codeforces.com/gym/106494/problem/B
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0422/solution/cf106494b.md
# 题目就是需要构造选择其他边之和大于最长边的几何图形
# 每条边都在[l,r]之间选择，则最长那条边就选l最大值




import init_setting
from lib.cflibs import *
def main():
    n = II()
    ls = LII()
    rs = LII()
    
    idx = ls.index(max(ls))
    ans = [0] * n
    
    total = 0
    for i in range(n):
        if i != idx:
            ans[i] = fmin(rs[i], ls[idx])
            total += ans[i]
        else: ans[i] = ls[i]
    
    if total >= ls[idx]: print(*ans)
    else: print(-1)