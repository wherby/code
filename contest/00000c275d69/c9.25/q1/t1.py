from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left
from functools import cache

class Solution(object):
    def lastMaterial(self, material):
        """
        :type material: List[int]
        :rtype: int
        """
        hp = []
        for a in material:
            heapq.heappush(hp,(-a,a))
        while len(hp)>=2:
            _,a = heapq.heappop(hp)
            _,b = heapq.heappop(hp)
            c = a-b 
            if c>0:
                heapq.heappush(hp,(-c,c))
            #print(hp)
        if len(hp) ==0:
            return 0
        else:
            return hp[0][1]





re =Solution().lastMaterial([10,2,6,1])
print(re)