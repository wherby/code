
from sortedcontainers import SortedDict,SortedList
from bisect import bisect_right,insort_left,bisect_left

class SL:
    def __init__(self,n):
        self.sl=[-1]
        for i in range(n):
            self.sl.append(i)
        self.sl.append(n)

    def remove(self,i):
        self.sl.remove(i)
    
    def next(self,i):
        k =bisect_left(self.sl,i)
        return self.sl[k+1]
    
    def pre(self,i):
        k = bisect_left(self.sl,i)
        return self.sl[k-1]

sl = SL(100)

sl.remove(2)
sl.remove(4)
sl.remove(3)
print(sl.next(1))
print(sl.pre(5))