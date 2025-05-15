from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache

import math
INF  = math.inf
import sys
sys.setrecursionlimit(100000)

class Solution:
    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        n = len(edges)+1
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(u, fu):
            tmp = [[0, 0] for _ in range(k+1)]
            for v in adj[u]:
                if v == fu:
                    continue
                t1 = dfs(v, u)
                for i in range(k):
                    tmp[i+1][0] += t1[i][0]
                    tmp[i+1][1] += t1[i][1]
            tmp[0][0] = tmp[k][1]*-1-nums[u]
            tmp[0][1] = tmp[k][0]*-1-nums[u]
            for i in range(1, k+1):
                tmp[i][0] += nums[u]
                tmp[i][1] += nums[u]
            for i in range(k-1, -1, -1):
                tmp[i][0] = max(tmp[i][0], tmp[i+1][0])
                tmp[i][1] = min(tmp[i][1], tmp[i+1][1])
            return tmp

        ans = dfs(0, -1)
        return ans[0][0]


# re =Solution().subtreeInversionSum( edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], nums = [4,-8,-6,3,7,-2,5], k = 2)
from input import edges,nums,k 
re = Solution().subtreeInversionSum(edges,nums,k)
print(re)