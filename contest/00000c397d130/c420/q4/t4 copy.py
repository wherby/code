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



    



class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        
        n = len(parent)
        g =[[] for  _ in range(n)]
        ans = [None]*n 
        def dfs(i):
            ret =[]
            for a in g[i]:    
                ret.append(dfs(a))
            ret.append(s[i])
            ret= "".join(ret)
            if ret == ret[::-1]:
                ans[i] = True
            else:
                ans[i] = False
            return ret
        for i,a in enumerate(parent):
            if a >=0:
                g[a].append(i)
        dfs(0)
        return ans
        





re =Solution().findAnswer(parent = [-1,3,0,2,9,7,1,2,7,12,0,7,7,12], s = "ikakdbhhgdbceb")
print(re)