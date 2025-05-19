# https://codeforces.com/problemset/problem/425/C
# https://github.com/Yawn-Sean/Daily_CF_Problems/blob/main/daily_problems/2025/05/0510/solution/cf425c.md
# 按照提意要求 DP(i,j) =N 的值
# 化简为按照 N 枚举， 每次遍历 DP(i) 求得最小的J 再计算

import sys
sys.path.append("..")
from cflibs.cflibs import *

from cflibs import *
def main():
    n, m, s, e = MII()
    nums1 = LII()
    nums2 = LII()

    pos = [[] for _ in range(100001)]

    for i in range(m):
        pos[nums2[i]].append(i)

    inf = 10 ** 6
    dp = [0] * (n + 1)
    ndp = [inf] * (n + 1)

    ans = 0

    for op in range(1, s // e + 1):
        cur = inf
        
        for i in range(1, n + 1):
            cur = fmin(cur, dp[i - 1])
            if cur < inf:
                if dp[i] > cur:
                    ndp[i] = dp[i]
                else:
                    p = bisect.bisect_left(pos[nums1[i - 1]], cur)
                    if p < len(pos[nums1[i - 1]]):
                        ndp[i] = pos[nums1[i - 1]][p] + 1
        
        for i in range(n + 1):
            dp[i] = ndp[i]
            ndp[i] = inf
        
        for i in range(1, n + 1):
            if dp[i] < inf and op * e + i + dp[i] <= s:
                ans = op

    print(ans)