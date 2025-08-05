# https://codeforces.com/problemset/problem/786/A
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/07/0730/solution/cf786a.md
# DP[i][pos] 表示轮到i在pos位置的时候，在选择移动前是什么状态
# 从获胜条件DFS-DP  从别人失败条件倒退,
#           如果上一个状态是自己状态未知情况下： 如果别人的状态是失败，则上一个自己的状态是成功，
#                                          如果别人的状态不是失败，则记录路径数量，如果所有路径都不能获胜，则自己上一个状态则是失败的

import init_setting
from lib.cflibs import *
def main():
    n = II()
    k1, *s1 = MII()
    k2, *s2 = MII()
    
    dp = [[0] * n for _ in range(2)]
    cnt = [[0] * n for _ in range(2)]
    
    def f(person, pos):
        return person * n + pos
    
    dp[0][0] = 2
    dp[1][0] = 2
    
    stk = []
    stk.append(f(0, 0))
    stk.append(f(1, 0))
    
    while stk:
        person, pos = divmod(stk.pop(), n)
        
        if person:
            for step in s1:
                last_pos = (pos - step) % n
                if dp[0][last_pos] == 0:
                    if dp[person][pos] == 2:
                        dp[0][last_pos] = 1
                        stk.append(f(0, last_pos))
                    else:
                        cnt[0][last_pos] += 1
                        if cnt[0][last_pos] == k1:
                            dp[0][last_pos] = 2
                            stk.append(f(0, last_pos))
        else:
            for step in s2:
                last_pos = (pos - step) % n
                if dp[1][last_pos] == 0:
                    if dp[person][pos] == 2:
                        dp[1][last_pos] = 1
                        stk.append(f(1, last_pos))
                    else:
                        cnt[1][last_pos] += 1
                        if cnt[1][last_pos] == k2:
                            dp[1][last_pos] = 2
                            stk.append(f(1, last_pos))
    
    strs = ['Loop', 'Win', 'Lose']
    print(' '.join(strs[dp[0][i]] for i in range(1, n)))
    print(' '.join(strs[dp[1][i]] for i in range(1, n)))