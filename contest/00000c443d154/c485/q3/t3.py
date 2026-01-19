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

class AuctionSystem:

    def __init__(self):
        self.bids = {}
        self.items = defaultdict(SortedList)
        

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        if (userId,itemId) in self.bids:
            oldM = self.bids[(userId,itemId)]
            self.items[itemId].remove((oldM,userId))
        self.bids[(userId,itemId)]  = bidAmount
        self.items[itemId].add((bidAmount,userId))

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        oldM  = self.bids[(userId,itemId)]
        self.items[itemId].remove((oldM,userId))
        self.items[itemId].add((newAmount,userId))
        self.bids[(userId,itemId)] =newAmount

    def removeBid(self, userId: int, itemId: int) -> None:
        oldM = self.bids[(userId,itemId)]
        self.items[itemId].remove((oldM,userId))
        del self.bids[(userId,itemId)]

    def getHighestBidder(self, itemId: int) -> int:
        t = self.items[itemId]
        if len(t) ==0:
            return -1 
        return t[-1][1]








re =Solution()
print(re)