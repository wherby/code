from sortedcontainers import SortedList
from bisect import bisect_right,bisect_left
class Span():
    def __init__(self):
        self.span =SortedList([(-1,-1),(10**10,10**10)])
    
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
        cnt = 0
        for item in remove:
            newLeft = min(newLeft,item[0])
            newRight = max(newRight,item[1])
            cnt += item[1]-item[0]+1
            self.span.remove(item)
        self.span.add((newLeft,newRight))
        return newRight-newLeft+1 -cnt

class CountIntervals(object):

    def __init__(self):
        self.cnt = 0
        self.sp = Span()


    def add(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        ac= self.sp.add(left,right)
        self.cnt += ac

    def count(self):
        """
        :rtype: int
        """
        return self.cnt

re = CountIntervals()
re.add(39,44)
re.add(13,49)
print(re.count())
re.add(47,50)
print(re.count())
print(re.sp.span)

re = CountIntervals()
re.add(2,3)
re.add(7,10)
print(re.count())
re.add(5,8)
print(re.count())
print(re.sp.span)