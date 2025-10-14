from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf

class ExamTracker:

    def __init__(self):
        self.rd = [0]
        self.time = [0]

        

    def record(self, time: int, score: int) -> None:
        self.time.append(time)
        self.rd.append(self.rd[-1] + score)

    def totalScore(self, startTime: int, endTime: int) -> int:
        k= bisect_right(self.time,endTime)
        k1 = bisect_right(self.time,startTime-1)
        return max(0,self.rd[k-1]-self.rd[k1-1])


# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)©leetcode




re =Solution()
print(re)