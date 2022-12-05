from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        ls = sentence.split(" ")
        n = len(ls)
        for i in range(n):
            if ls[i][0] != ls[i-1][-1]:
                return False
        return True





re =Solution()
print(re)