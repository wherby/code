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

from input import nums

class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        mod = 10**9+7
        n = len(conversions)+1
        ret = [-1]*n 
        g = [[] for _ in range(n)] 
        for a,b,c in conversions:
            g[a].append((b,c))
        st = deque([(0,1)])
        visit ={}
        while st:
            a,c1 = st.popleft()
            if a in visit:
                continue
            visit[a] =1
            ret[a] = c1 
            for b,c in g[a]:
                if b not in visit:
                    st.append((b,c*c1%mod))

        return ret
        





re =Solution().baseUnitConversions(nums)
print(re)