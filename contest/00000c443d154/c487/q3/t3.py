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

class RideSharingSystem:

    def __init__(self):
        self.riders = deque()
        self.drivers= deque()
        self.rmr ={}
        self.rd = {}
        

    def addRider(self, riderId: int) -> None:
        self.riders.append(riderId)
        self.rd[riderId]=1
        

    def addDriver(self, driverId: int) -> None:
        self.drivers.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        while self.riders and self.riders[0] in self.rmr:
            self.riders.popleft()
        if not self.riders or not self.drivers:
            return [-1,-1]
        r = self.riders.popleft()
        d = self.drivers.popleft()
        return [d,r]

    def cancelRider(self, riderId: int) -> None:
        if riderId in self.rd:
            self.rmr[riderId]=1


re =Solution()
print(re)