from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        acc= 0
        vowls=set(['a', 'e', 'i', 'o',  'u'])
        for i in range(left,right+1):
            a =words[i]
            if a[0] in vowls and a[-1] in vowls:
                acc+=1
        return acc





re =Solution()
print(re)