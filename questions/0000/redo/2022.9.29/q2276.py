# https://leetcode.com/contest/weekly-contest-293/problems/count-integers-in-intervals/

from sortedcontainers import SortedList
from bisect import bisect_right,bisect_left
class Span():
    def __init__(self):
        self.span =SortedList([(-1,-1),(10**10,10**10)])
        self.cnt =0
    
    def add(self,left,right):
        leftIdx = bisect_left(self.span,(left,0))
        leftIdx -=1
        if self.span[leftIdx][1] <left-1:
            leftIdx +=1
        remove=[]
        endIdx = leftIdx
        while  endIdx < len(self.span) and self.span[endIdx][0] <=right +1:
            remove.append(self.span[endIdx])
            endIdx +=1
        newLeft,newRight = left,right
        for item in remove:
            newLeft = min(newLeft,item[0])
            newRight = max(newRight,item[1])
            self.span.remove(item)
            self.cnt -= item[1]-item[0]+1
        self.span.add((newLeft,newRight))
        self.cnt += newRight-newLeft +1
        
class CountIntervals(object):

    def __init__(self):
        self.span =Span()

    def add(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        self.span.add(left,right)
        

    def count(self):
        """
        :rtype: int
        """
        return self.span.cnt


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()