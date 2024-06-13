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
    def clearStars(self, s: str) -> str:
        dic ={}
        ls = [deque([]) for _ in range(26)]
        for i,a in enumerate(s):
            if a == "*":
                dic[i] =1 
                for j in range(26):
                    if len(ls[j]) >0:
                        k=ls[j].popleft()
                        dic[k] =1 
                        break
            else:
                ls[ord(a)-ord('a')].append(i)
        ret =[]
        for i in range(len(s)):
            if i not in dic:
                ret.append(s[i])
        return "".join(ret)





re =Solution().clearStars( "aaba*")
print(re)