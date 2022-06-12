from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution(object):
    def calculateTax(self, brackets, income):
        """
        :type brackets: List[List[int]]
        :type income: int
        :rtype: float
        """
        sm = 0
        st =0
        for a,p in brackets:
            if income>a:
                sm += (a-st)*1.00 /100 *p
                st = a 
            else:
                sm += (income-st)*1.00 /100 *p
                st = a 
                break
        return sm

re =Solution().calculateTax(brackets = [[1,0],[4,25],[5,50]], income = 2)
print(re)