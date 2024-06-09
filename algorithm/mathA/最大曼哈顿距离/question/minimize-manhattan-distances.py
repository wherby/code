# https://leetcode.cn/contest/weekly-contest-391/problems/minimize-manhattan-distances/
# https://leetcode.cn/problems/minimize-manhattan-distances/solutions/2716755/tu-jie-man-ha-dun-ju-chi-heng-deng-shi-b-op84/

from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf



class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        xs= SortedList([])
        ys= SortedList([])
        
        for x,y in points:
            xs.add(x+y)
            ys.add(x-y)
        
        ans = 10**23
        for x,y in points:
            x,y = x+y,x-y 
            xs.remove(x)
            ys.remove(y)
            ans = min(ans, max(xs[-1]-xs[0],ys[-1]-ys[0]))
            xs.add(x)
            ys.add(y)
        return ans
                
            





re =Solution().minimumDistance(points = [[3,10],[5,15],[10,2],[4,4]])
print(re)