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

class Spreadsheet:

    def __init__(self, rows: int):
        self.dic=defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        self.dic[cell] = value

    def resetCell(self, cell: str) -> None:
        self.dic[cell] = 0

    def getValue(self, formula: str) -> int:
        a,b = formula.split("+")
        a = a[1:]
        def getN(tk):
            if tk[0].isalpha():
                return self.dic[tk]
            else:
                return int(tk)
        return getN(a)+getN(b)


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)©leetcode





re =Solution()
print(re)