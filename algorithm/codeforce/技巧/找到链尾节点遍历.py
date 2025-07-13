# https://codeforces.com/problemset/problem/316/B2
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0711/solution/cf316b2.md
# 如果一个记录了pre 的数组， 怎么找到所有的链尾， 用 note 数组标记链尾值，如果pre出现了这个节点，这个节点就不是链尾，标记完之后剩下的节点就是链尾
# 链的合并，就是背包dp

import sys
sys.path.append("..")
from cflibs.cflibs import *
def main():
    n, pos = MII()
    pos -= 1

    prev = LGMI()
    note = [1] * n

    for i in range(n):
        if prev[i] >= 0:
            note[prev[i]] = 0

    tmp = []
    relative_pos = -1

    for i in range(n):
        if note[i]:
            cur = i
            cnt = 0
            flg = False
            
            while cur >= 0:
                cnt += 1
                if cur == pos:
                    flg = True
                    relative_pos = cnt
                cur = prev[cur]
            
            if flg: relative_pos = cnt + 1 - relative_pos
            else: tmp.append(cnt)

    dp = [0] * (n + 1)
    dp[0] = 1

    for x in tmp:
        for i in range(n, x - 1, -1):
            if dp[i - x]:
                dp[i] = 1

    print('\n'.join(str(i + relative_pos) for i in range(n + 1) if dp[i]))