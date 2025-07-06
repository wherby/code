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

import re
class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        business_order = {
        "electronics": 0,
        "grocery": 1,
        "pharmacy": 2,
        "restaurant": 3
        }
        ret = []
        for i in range(len(code)):
            if not isActive[i]:continue
            if businessLine[i] not in business_order:continue
            if not code[i] or not re.fullmatch(r'^[a-zA-Z0-9_]+$', code[i]):
                continue
            ret.append((code[i],businessLine[i]))
        ret.sort(key = lambda x:(business_order[x[1]],x[0]))
        ret = [x[0] for x in ret]
        return ret




re =Solution().validateCoupons( code = ["SAVE20","","PHARMA5","SAVE@20"], businessLine = ["restaurant","grocery","pharmacy","restaurant"], isActive = [True,True,True,True])
print(re)