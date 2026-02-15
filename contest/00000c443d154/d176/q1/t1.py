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
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ret =[]
        for word in words:
            acc = 0 
            for a in word:
                acc += weights[ord(a) - ord('a')]
            acc = acc %26
            ret += chr(25-acc + ord('a'))
        return "".join(ret)





re =Solution()
print(re)