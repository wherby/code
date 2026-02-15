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
    def prefixConnected(self, words: List[str], k: int) -> int:
        dic =defaultdict(list)
        cnt =0
        for word in words:
            if len(word)<k:continue
            dic[word[:k]].append(word)
        for _,vs in dic.items():
            if len(vs)>=2:
                cnt +=1
        return cnt



