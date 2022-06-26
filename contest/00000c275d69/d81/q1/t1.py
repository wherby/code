from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution:
    def countAsterisks(self, s: str) -> int:
        cnt =0
        start =0
        for a in s:
            if a =="|":
                start +=1
            if a =="*" and start%2 ==0:
                cnt +=1
        return cnt