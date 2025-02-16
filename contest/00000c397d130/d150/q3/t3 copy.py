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


def find_horizontal_line(events):
    
    
    # Sort events by y-coordinate
    events.sort()
    
    # Initialize active intervals and total area
    active = SortedList([])
    total_area = 0
    prev_y = None
    psm = None
    for event in events:
        y, typ, x1, x2 = event

        
        if typ == 'start':
            active.add((x1,+1))
            active.add((x2,-1))
        else:
            active.remove((x1,+1))
            active.remove((x2,-1))
        
        acc = 0 
        sm =0
        lst = -1
        for a,t in active:
            if acc ==0:
                lst =a 
                acc += t 
            else:
                sm += a -lst
                lst = a 
                acc += t
        if psm != None:
            total_area += psm *(y-prev_y)
        #print(active,y,total_area)
        prev_y = y
        psm = sm
    
    return total_area


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        for x, y, l in squares:
            events.append((y, 'start', x, x + l))
            events.append((y + l, 'end', x, x + l))
        totalS = find_horizontal_line(events)


        def verify(mid):
            sm = 0 
            events = []
            for x,y,l in squares:
                if y > mid: continue 
                t = min(y+l,mid)
                events.append((y, 'start', x, x + l))
                events.append((t, 'end', x, x + l))
            return find_horizontal_line(events) *2
        l,r = 0,10**10

        while l + 10**(-6) <r:
            mid = (l+r)/2
            t= verify(mid)
            if t >=totalS:
                r= mid 
            elif t < totalS:
                l = mid 
            #print(l,r)
        return l





re =Solution().separateSquares(squares = [[0,0,2],[1,1,1]])
print(re)