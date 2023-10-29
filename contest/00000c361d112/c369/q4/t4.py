from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        n = len(coins)
        g = [[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        @cache
        def dfs(i,c,p):
            mx = coins[i]//c-k
            for a in g[i]:
                if a ==p:continue
                mx += dfs(a,c,i)
            b = coins[i] //(c*2)
            for a in g[i]:
                if a ==p:continue
                b += dfs(a,min(c*2,10**5),i)
            #print(i,max(b,mx),c,b,mx)
            return max(b,mx)
        return dfs(0,1,-1)




#re =Solution().maximumPoints(edges = [[0,1],[1,2],[2,3]], coins = [10,10,3,3], k = 5)
re = Solution().maximumPoints([[1,0],[0,2],[1,3]],[9,3,8,9],0)
print(re)