from collections import defaultdict
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        n = len(seats)
        seats = sorted(seats)
        students = sorted(students)
        num =0
        for i in range(n):
            num += abs(seats[i] - students[i])
        return num 