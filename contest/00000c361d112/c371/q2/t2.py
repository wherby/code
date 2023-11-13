from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        def getV(s1):
            return int(s1[:2])*60 + int(s1[2:])
        dic = defaultdict(list)
        for na,ts in access_times:
            dic[na].append(getV(ts))
        res = []
        for k,v in dic.items():
            v.sort()
            m = len(v)
            for i in range(m-2):
                if v[i+2]-v[i]<60:
                    res.append(k)
                    break
        return res





re =Solution()
print(re)