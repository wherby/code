# https://leetcode.cn/problems/minimum-cost-to-merge-sorted-lists/

from typing import List, Tuple, Optional

from functools import cache


from bisect import bisect_right,insort_left,bisect_left


import time


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0 
        name = func.__name__
        arg_str = ", ".join(repr(arg) for arg in args)
        print('[{0}] {1}' .format( elapsed, name))
        return result
    return clocked

from input import lists,lists2


class Solution:
    @clock
    def minMergeCost(self, lists: List[List[int]]) -> int:
        n = len(lists)
        N = 1<<n
        sum_len = [0]*N 
        sorted =[[] for _ in range(N)]
        median = [0]*N 

        for i,a in enumerate(lists):
            high_bit = 1<<i 
            for s in range(high_bit):
                t = high_bit | s 
                sum_len[t] = sum_len[s] + len(a)
                b = sorted[s] + a 
                b.sort()
                sorted[t] = b 
                median[t] = b[(len(b) -1)//2]
        dp = [10**20 ]* N 

        for i in range(N):
            if i & (i-1) ==0:
                dp[i] = 0 
                continue
            # 枚举 i 的非空真子集 j
            j = i&(i-1)
            while j > (i^j):
                k = i^j
                dp[i] = min(dp[i], dp[j] + dp[k] + sum_len[i]+ abs(median[j] - median[k]) )
                j = (j-1)&i
        return dp[-1]


from input import lists2
re =Solution().minMergeCost(lists2)
print(re)