from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
from itertools import pairwise

class Solution:
    def countDigits(self, num: int) -> int:
        return len([i for i in str(num) if num% int(i)==0])





re =Solution().countDigits(121)
print(re)