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
    def majorityFrequencyGroup(self, s: str) -> str:
        c = Counter(s)
        dic = defaultdict(list)
        for k,v in c.items():
            dic[v].append(k)
        ret  =""
        ls =[]
        for k,v in dic.items():
            ls.append((len(v),k,v))
        ls.sort()
        return "".join(ls[-1][2])




re =Solution()
print(re)