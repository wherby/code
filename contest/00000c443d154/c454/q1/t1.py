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
    def generateTag(self, caption: str) -> str:
        ls = caption.split(" ")
        ls = [a for a in ls if len(a.strip())>0]
        if len(ls) ==0:
            return ""
        ret = []
        for a in ls:
            a = a.lower()
            a=a.capitalize()
            ret.append(a)
        ret[0] =ret[0].lower()
        res = "#" +"".join(ret)
        return res[:100]





re =Solution().generateTag("  ")

print(re)