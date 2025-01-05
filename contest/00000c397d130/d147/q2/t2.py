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

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.dic = SortedList([])
        self.fd={}
        for u,t,p in tasks:
            self.dic.add((p,t,u))
            self.fd[t] =(u,p)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.fd[taskId] = (userId, priority)
        self.dic.add((priority,taskId,userId))
        

    def edit(self, taskId: int, newPriority: int) -> None:
        u,op = self.fd[taskId]
        self.dic.remove((op,taskId,u))
        self.dic.add((newPriority,taskId,u))
        self.fd[taskId] = (u,newPriority)
        

    def rmv(self, taskId: int) -> None:
        u,op = self.fd[taskId]
        self.dic.remove((op,taskId,u))
        del self.fd[taskId]

    def execTop(self) -> int:
        if len(self.dic) ==0:
            return -1
        p,t,u = self.dic.pop()
        return u


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()©leetcode




re =Solution()
print(re)