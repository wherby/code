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
    def separateSquares(self, squares: List[List[int]]) -> float:
        acc = 0
        for x,y,l in squares:
            acc += l*l 
        
        #print(acc)
        def verify(mid):
            sm = 0 
            for x,y,l in squares:
                if y > mid: continue 
                t = min(y+l,mid)
                sm += (t-y)*l 
            return sm *2
        l,r = 0,10**10

        while l + 10**(-6) <r:
            mid = (l+r)/2
            t= verify(mid)
            if t >=acc:
                r= mid 
            elif t < acc:
                l = mid 
            #print(l,r)
        return l



nums = [[522261215,954313664,461744743],[628661372,718610752,21844764],[619734768,941310679,91724451],[352367502,656774918,591943726],[860247066,905800565,853111524],[817098516,868361139,817623995],[580894327,654069233,691552059],[182377086,256660052,911357],[151104008,908768329,890809906],[983970552,992192635,462847045]]

re =Solution().separateSquares(nums)
print(re)