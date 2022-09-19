from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left
from functools import cache

class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        dic = {}
        for i,a in enumerate(s):
            k = ord(a)-ord('a')
            if k not in dic:
                dic[k] = i 
            else:
                t = i - 1-dic[k]
                if t != distance[k]:
                    return False
        return True





re =Solution()
print(re)