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

class Solution:
    def countPairs(self, words: List[str]) -> int:
        dic = defaultdict(int)
        def getNext(s1):
            ret = []
            for i in range(26):
                res = [] 
                for a in s1:
                    t = (ord(a) -ord('a') + i) %26 
                    t = chr(ord('a') +t)
                    res.append(t)
                ret.append("".join(res))
            return ret 
        cnt = 0
        for s1 in words:
            for b in getNext(s1):
                cnt += dic[b]
            dic[s1] +=1
        return cnt



re =Solution().countPairs(["ab","aa","za","aa"])
print(re)