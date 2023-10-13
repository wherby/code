from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        dic=defaultdict(int)
        cnt = 0
        for a,b in coordinates:
            for l in range(k+1):
                r = k-l
                c,d= a ^ l,b^ r
                cnt += dic[(c,d)]
            dic[(a,b)] +=1
        return cnt





re =Solution().countPairs(coordinates = [[1,2],[4,2],[1,3],[5,2]], k = 5)
print(re)