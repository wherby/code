from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue

class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money<children:
            return -1
        onlyOne= money ==(children-1)*8+4
        moreOne = children*8 <money
        #print(moreOne)
        return min((money-children)//7,children)-onlyOne-moreOne




re =Solution().distMoney(117,2)
print(re)