from collections import defaultdict,deque
import functools
import heapq
from math import gcd
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left
from functools import cache

class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        cnt = 0
        for i in range(1,min(a,b)+1):
            if a%i ==b%i==0:
                cnt +=1
        return cnt




re =Solution().commonFactors(12,6)
print(re)