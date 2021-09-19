from collections import defaultdict
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
import functools


class Solution:
    def finalValueAfterOperations(self, operations):
        cnt = 0
        for o in operations:
            if o.find("+")>=0:
                cnt+=1
            else:
                cnt -=1
        return cnt