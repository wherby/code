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
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        dh = [(d,(h+power-1)//power) for d,h in zip(damage,health)]
        st = []
        for i,(d,h) in enumerate(dh):
            heappush(st,(h/d,i,d,h))
        allD = sum(damage)
        sm =0
        while st:
            _,i,d,h = heappop(st)
            sm += h*allD 
            allD -=d
        return sm


# (x+a+b)*(b1)//c +(x+a)*a1//c  - [(x+a+b)*(a1)//c +(x+b)*b1//c]
# (a+b)*b1 + a*a1 - [(a+b)*a1 + b*b1]
# (a+b)(b1-a1) 
# ab1 + bb1 -aa1-ba1 + aa1- bb1
# ab1-ba1
# b1/b-a1/a


re =Solution().minDamage(power = 4, damage = [1,2,3,4], health = [4,5,6,8])
print(re)