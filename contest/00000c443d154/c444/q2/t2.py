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

class Router:

    def __init__(self, memoryLimit: int):
        self.n =memoryLimit
        self.ls = deque([])
        self.dic = {}
        self.ddic = defaultdict(deque)
        

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        b =(source,destination,timestamp)
        if b in self.dic:
            return False
        if len(self.ls) ==self.n:
            a= self.ls.popleft()
            self.ddic[a[1]].popleft()
            del self.dic[a]
        self.ls.append(b)
        self.dic[b] =1
        self.ddic[b[1]].append(b[2])
        return True
        

    def forwardPacket(self) -> List[int]:
        if len(self.ls) ==0:
            return []
        b = self.ls.popleft()
        del self.dic[b]
        self.ddic[b[1]].popleft()
        return [b[0],b[1],b[2]]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        k1 = bisect_left(self.ddic[destination],startTime)
        k2 = bisect_right(self.ddic[destination],endTime)
        return k2-k1


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)©leetcode





re =Solution()
print(re)