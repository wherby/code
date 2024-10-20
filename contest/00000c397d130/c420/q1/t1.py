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


atoz = 'abcdefghijklmnopqrstuvwxyz'
class Solution:
    def stringSequence(self, target: str) -> List[str]:
        dic = {}
        for i,a in enumerate(atoz):
            dic[a] = i 
        ret= []
        pre = ""
        for a in target:

            for j in range(dic[a]+1):
                ret.append(pre+atoz[j])

            pre = pre + a 
        return ret




re =Solution().stringSequence("z")
print(re)