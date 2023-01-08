from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution(object):
    def categorizeBox(self, length, width, height, mass):
        """
        :type length: int
        :type width: int
        :type height: int
        :type mass: int
        :rtype: str
        """
        b = max(length,height,width)>=10**4 or length*width*height>= 10**9
        h = mass>=100
        if b and h: return "Both"
        if not b and not h : return "Neither"
        if b: return "Bulky"
        if h: return "Heavy"




re =Solution()
print(re)