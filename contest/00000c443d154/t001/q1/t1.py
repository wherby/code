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
    pass


A ="BUUBDLA PSSPABUAEBXO"
A= [ord(a) -ord("A") for a in A]
ls=[chr(ord('A') +(a+26)%27) for a in A]

print(ls)




re =Solution()
print(re)