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
    def isValid(self, word: str) -> bool:
        vowls=set(['a', 'e', 'i', 'o',  'u'])
        for a in word:
            if not(a.isdigit() or a.isalpha()):
                return False
        return  len(word)>=3 and len([a.lower() for a in word if a.lower() in vowls]) >=1 and len([a for a in word if a.lower() not in vowls and a.isalpha()]) >=1




re =Solution().isValid("AhI")
print(re)