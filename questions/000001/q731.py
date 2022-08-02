import heapq
class MyCalendarTwo(object):

    def __init__(self):
        self.st=[]


    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        newHeap = list(self.st)
        heapq.heappush(newHeap, (start,1))
        heapq.heappush(newHeap, (end-0.1,-1))
        acc =0
        while newHeap:
            _, diff = heapq.heappop(newHeap)
            acc += diff
            if acc >=3:
                return False
        heapq.heappush(self.st, (start,1))
        heapq.heappush(self.st, (end-0.1,-1))
        return True