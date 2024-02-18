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
from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter(word)
        ret =0
        cnt = 0
        ls = list(c.values())
        ls.sort(reverse=True)
        #print(ls)
        for a in ls :
            
            ret += ((cnt//8)+1)*a 
            cnt +=1 
        return ret




re =Solution().minimumPushes("xycdefghij")
print(re)