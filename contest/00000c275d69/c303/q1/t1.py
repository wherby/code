from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left
from functools import cache
from sortedcontainers import SortedList

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        sm = 10**10
        dic ={}
        for i,a in  enumerate(s):
            if a in dic:
                return a
            dic[a] =1





re =Solution()
print(re)