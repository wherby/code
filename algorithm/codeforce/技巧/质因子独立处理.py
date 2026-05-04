# https://codeforces.com/gym/106507/problem/H
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2026/04/0430/solution/cf106507h.md
# 题目中每次操作只能影响一个质数因子，所以每个质数因子在操作上是独立的，可以用类似背包DP处理


import init_setting
from cflibs import *
def main():
    M = 10 ** 6 + 5
    pr = list(range(M))
    
    for i in range(2, M):
        if pr[i] == i:
            for j in range(i, M, i):
                pr[j] = i
    
    n, k = MII()
    nums = LII()
    
    cnt = [0] * M
    
    for x in nums:
        while x > 1:
            cnt[pr[x]] += 1
            x //= pr[x]
    
    dp = [1] * (k + 1)
    
    for i in range(M):
        if cnt[i] >= n:
            
            pws = [0] * 20
            for x in nums:
                pw = 0
                while x % i == 0:
                    x //= i
                    pw += 1
                pws[pw] += 1
    
            transitions = []
            val = 1
            
            for a in range(cnt[i] // n + 1):
                cost = 0
                for b in range(a):
                    cost += (a - b) * pws[b]
                transitions.append((cost, val))
                val *= i
            
            for i in range(k, -1, -1):
                dp_val = dp[i]
                for cost, val in transitions:
                    if i >= cost:
                        dp_val = fmax(dp_val, dp[i - cost] * val)
                dp[i] = dp_val
    
    print(' '.join(map(str, dp[1:])))