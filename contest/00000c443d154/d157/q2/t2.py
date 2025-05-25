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
    def maxSubstrings(self, word: str) -> int:
        cnt = 0
        dic = {}
        for i,a in enumerate(word):
            if a in dic and i- dic[a]>=3:
                cnt +=1
                dic={}
            elif a not in dic:
                dic[a] = i 
            #print(dic)
        return cnt





re =Solution().maxSubstrings("abcdeafdef")
print(re)