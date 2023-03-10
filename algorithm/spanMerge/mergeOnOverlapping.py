
from typing import List, Tuple, Optional

from sortedcontainers import SortedList
from bisect import bisect_right,bisect_left

## Merge on overlapping [[0,0][1,1]] will not merge
class Span():
    def __init__(self):
        self.span =SortedList([(-3,-2),(10**10,10**10)])
    
    def add(self,left,right):
        leftIdx = bisect_left(self.span,(left,0))
        leftIdx -=1
        if self.span[leftIdx][1] <left:
            leftIdx +=1
        remove=[]
        endIdx = leftIdx
        while  endIdx < len(self.span) and self.span[endIdx][0] <=right :
            remove.append(self.span[endIdx])
            endIdx +=1
        newLeft,newRight = left,right
        for item in remove:
            newLeft = min(newLeft,item[0])
            newRight = max(newRight,item[1])
            self.span.remove(item)
        self.span.add((newLeft,newRight))
        
class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        sp = Span()
        for a,b in ranges:
            sp.add(a,b)
        n = len(sp.span)-2
        #print(sp.span)
        mod = 10**9+7
        re = pow(2,n,mod)
        return re




re =Solution().countWays(ranges = [[0,0],[8,9],[12,13],[1,3]])
print(re)