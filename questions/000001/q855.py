from itertools import pairwise
from sortedcontainers import SortedDict,SortedList
class ExamRoom(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.n = n
        self.sl=SortedList([])

    def seat(self):
        """
        :rtype: int
        """
        if len(self.sl) == 0:
            self.sl.add(0)
            return 0 
        diff,idx =self.sl[0],0
        for x,y in pairwise(self.sl):
            if (y-x) //2 >diff:
                diff =(y-x)//2
                idx = x + diff
        if self.n-1 - self.sl[-1] > diff:
            diff = self.n-1 - self.sl[-1]
            idx = self.n -1
        self.sl.add(idx)
        return idx


    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        self.sl.remove(p)