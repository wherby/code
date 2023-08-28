# https://leetcode.cn/problems/merge-intervals/submissions/
from sortedcontainers import SortedList
from typing import List, Tuple, Optional
from bisect import bisect_right,bisect_left
## Merge on continue [[1,1][2,2]] will not merge
class Span():
    def __init__(self):
        self.span =SortedList([(-1,-1),(10**10,10**10)])
    
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
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sp = Span()
        for a,b in intervals:
            sp.add(a,b)
        return sp.span[1:-1]


re =Span()
re.add(1,1)
re.add(2,2)
re.add(3,3)
re.add(5,8)
re.add(7,10)
print(re.span)
        