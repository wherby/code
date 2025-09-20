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



from collections import defaultdict
from math import gcd

MOD = 10**9 + 7

# y = (dy/dx)*x +b
# b = (y*dx-dy*x)/dx

def get_slope(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    if dx == 0 and dy == 0:
        return (0, 0)
    if dx == 0:
        return (1, 0)  # vertical line
    if dy == 0:
        return (0, 1)  # horizontal line
    g = math.gcd(dy, dx)
    dy //= g
    dx //= g
    if dx < 0:
        dy *= -1
        dx *= -1
    return (dy, dx)
from math import inf
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        dic1 = defaultdict(lambda: defaultdict(int))
        dic2 = defaultdict(lambda: defaultdict(int))
        for i,(x,y) in enumerate(points):
            for x2,y2 in points[:i]:
                dy,dx =get_slope([x,y],[x2,y2])
                if dx == 0:
                    b = x
                else:
                    b = (y*dx - x*dy)/dx
                dic1[(dy,dx)][b] +=1
                dic2[(x+x2,(y+y2))][(dy,dx)] +=1
        cnt = 0
        for k in dic1:
            acc = 0 
            for b in dic1[k].values():
                cnt += b*acc 
                acc +=b 
        for k in dic2:
            acc=0 
            for b in dic2[k].values():
                cnt -= acc*b
                acc +=b 
        return cnt



re =Solution().countTrapezoids([[-3,2],[3,0],[2,3],[3,2],[2,-3]])
print(re)