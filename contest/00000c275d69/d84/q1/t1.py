from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left
from functools import cache

class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        dic = defaultdict(int)
        for a,b in items1:
            dic[a]+=b
        for a,b in items2:
            dic[a]+=b
        ret = []
        for a,b in dic.items():
            ret.append([a,b])
        ret.sort()
        return ret





re =Solution()
print(re)