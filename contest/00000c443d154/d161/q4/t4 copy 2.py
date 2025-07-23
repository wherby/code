from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf


mx = 100
dp=[0]*(mx+1)
dp[1] = 0
for i in range(2,mx+1):
    dp[i]=dp[i.bit_count()]+1
print(dp)
class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        if k==0:
            return 1
        n = len(s)

        @cache
        def dfs(i: int, left1: int, is_limit: bool) -> int:
            if i == n:
                return 0 if is_limit or left1 else 1
            up = int(s[i]) if is_limit else 1
            res = 0
            for d in range(min(up, left1) + 1):
                res += dfs(i + 1, left1 - d, is_limit and d == up)
            return res

        ans = 0
        f = [0] * n
        for i in range(1, n):
            f[i] = f[i.bit_count()] + 1
            if f[i] <= k:
                # 计算有多少个二进制数恰好有 i 个 1
                ans += dfs(0, i, True)
        dfs.cache_clear()  # 防止爆内存
        return ans


    def popcountDepth(self, n: int, k: int) -> int:
        if k==0:
            return 1
        s=bin(n+1)[2:]
        return self.countKReducibleNumbers(s,k)-self.countKReducibleNumbers(s,k-1)
            
        
        






re =Solution().popcountDepth(4,1)
print(re)