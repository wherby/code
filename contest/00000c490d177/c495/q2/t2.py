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

class EventManager:

    def __init__(self, events: list[list[int]]):
        self.sl =SortedList([])
        self.dic= {}
        for id,p in events:
            self.sl.add((-p,id))
            self.dic[id] = p 
        

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        op = self.dic[eventId]
        self.sl.remove((-op,eventId))
        self.dic[eventId] = newPriority
        self.sl.add((-newPriority,eventId))
        

    def pollHighest(self) -> int:
        if len(self.sl) ==0:
            return -1 
        p,eid = self.sl[0]
        self.sl.remove((p,eid))
        del self.dic[eid]
        return eid




re =Solution()
print(re)