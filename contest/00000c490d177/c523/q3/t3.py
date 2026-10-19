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

class BusBooking:

    def __init__(self, n: int):
        self.total = 0
        self.cnt = 0 
        self.dict ={}
        self.cost ={}

    def toggle(self, seat: str) -> None:
        if seat not in self.dict:
            A,IDX = seat[0],seat[1:]
            B =A
            if A =="A":
                B = "B"
            if A =="D":
                B="C"
            if B+IDX not in self.dict:
                self.total +=1
                self.cost[seat] =1
            else:
                self.total +=3
                self.cost[seat] = 3 
            self.dict[seat] =1 
            self.cnt +=1
        else:
            del self.dict[seat]
            self.cnt -=1
            self.total -= self.cost[seat]
            
    def getTotalTime(self) -> int:
        return self.total

    def getMinTime(self) -> int:
        return self.cnt


# Your BusBooking object will be instantiated and called as such:
# obj = BusBooking(n)
# obj.toggle(seat)
# param_2 = obj.getTotalTime()
# param_3 = obj.getMinTime()©leetcode




re =Solution()
print(re)