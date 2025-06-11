# https://codeforces.com/problemset/problem/639/D
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/06/0607/solution/cf639d.md
# 题目需要求+5.+1 使得k个值相等的最小代价，使用同余的方法分析，在用窗口加前缀方法求得各种情况的代价

import sys
sys.path.append("..")
from cflibs.cflibs import *

def main():
    n, k, b, c = MII()
    b = min(b, 5 * c)

    nums = LII()
    nums.sort()

    ans = 10 ** 18

    for i in range(5):
        pq = []
        total = 0
        
        for v in nums:
            cur = 0
            while v % 5 != i:
                v += 1
                cur += c
            
            v = (v - i) // 5
            
            heappush(pq, v * b - cur)
            total += v * b - cur
            
            while len(pq) > k:
                total -= heappop(pq)
            
            if len(pq) == k:
                ans = fmin(ans, v * b * k - total)

    print(ans)