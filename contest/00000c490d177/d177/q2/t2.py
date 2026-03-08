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
    def mergeCharacters(self, s: str, k: int) -> str:
        def merge(s1):
            dic = {}
            for i,a in enumerate(s1):
                if a not in dic:
                    dic[a] = i
                elif i - dic[a] <= k:
                    return s1[:dic[a]] + s1[dic[a]+1:i] + s1[i+1:]
                else:
                    dic[a] = i
            return s1
        while len(s)!= len(merge(s)):
            s = merge(s)
        return s





re =Solution()
print(re)