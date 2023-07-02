from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        dic = defaultdict(int)
        cnt =0
        for a in words:
            ra = a[::-1]
            if dic[ra] ==0:
                dic[a] +=1
            else:
                dic[ra] -=1
                cnt +=1
            #print(dic)
        return cnt





re =Solution().maximumNumberOfStringPairs(words = ["cd","ac","dc","ca","zz"])
print(re)