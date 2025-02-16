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
    active =  SortedList([])
    total_area = 0
    prev_y = None
    psm = None
    sm = 0
    for event in events:
        y, typ, x1, x2 = event

        
        if typ == 'astart':
            active.add((x1,+1))
            active.add((x2,-1))
            k1 = bisect_left(active,(x1,+1))
            k2 = active.bisect_left((x2,-1))
        else:
            k1 = bisect_left(active,(x1,+1))
            k2 = active.bisect_left((x2,-1))

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

dicx = {}
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        mxy = 0
        xs =set([])
        for x, y, l in squares:
            events.append((y, 'astart', x, x + l))
            events.append((y + l, 'end', x, x + l))
            xs.add(x)
            xs.add(x+l)
            mxy= max(mxy,y+l)
        totalS = find_horizontal_line(events)
        xs = list(xs)
        
        xs.sort()
        for i,a in enumerate(xs):
            dicx[a] = i
        

        def verify(mid):
            sm = 0 
            events = []
            for x,y,l in squares:
                if y > mid: continue 
                t = min(y+l,mid)
                events.append((y, 'astart', x, x + l))
                events.append((t, 'end', x, x + l))
            return find_horizontal_line(events) *2
        l,r = 0,mxy*2

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