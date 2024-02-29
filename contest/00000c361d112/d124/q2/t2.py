from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        dic=defaultdict(list)
        for i,a in enumerate(s):
            dic[a].append(i)
        mx = 0
        for k in dic.keys():
            mx = max(mx,len(dic[k]))
        ret =[]
        for k in dic.keys():
            if len(dic[k]) ==mx:
                ret.append((dic[k][-1],k))
        ret.sort()
        res =""
        for _,a in ret:
            res=res+a 
        return res
        





re =Solution().lastNonEmptyString("aabcbbca")
print(re)