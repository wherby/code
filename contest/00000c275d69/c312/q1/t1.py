from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left
from functools import cache

class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        return [na[0] for na in sorted(zip(names,heights),key=lambda x:x[1],reverse=True)]





re =Solution().sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170])
print(re)