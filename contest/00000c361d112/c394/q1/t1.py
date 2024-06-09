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

import string
from collections import Counter
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        c = Counter(word)
        cnt = 0
        atoz = list(string.ascii_lowercase)
        atoz2 = list(string.ascii_uppercase)
        for i,a in enumerate(atoz):
            if a in c and atoz2[i] in c:
                cnt +=1
        return cnt





re =Solution()
print(re)