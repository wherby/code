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
        for item in remove:
            newLeft = min(newLeft,item[0])
            newRight = max(newRight,item[1])
            self.span.remove(item)
        self.span.add((newLeft,newRight))
        
class LUPrefix(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.sp = Span()


    def upload(self, video):
        """
        :type video: int
        :rtype: None
        """
        self.sp.add(video,video)


    def longest(self):
        """
        :rtype: int
        """
        if self.sp.span[1][0] != 1:
            return 0
        return self.sp.span[1][1] - self.sp.span[1][0] +1



# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()



a = LUPrefix(4)
re =a.upload(3)
print(a.longest())