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
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        bls = bin(k-1)[2:][::-1]
        acc =0
        for i, a in enumerate(bls):
            if a =="1" and operations[i] ==1:
                acc +=1
        return chr(ord('a') + acc%26)




re =Solution().kthCharacter(k = 3, operations = [1,0,0,1])
print(re)