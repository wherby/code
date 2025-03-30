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
    def longestPalindrome(self, s: str, t: str) -> int:
        
        def getSub(s):
            n =len(s)
            sb =[""]
            for i in range(n):
                for j in range(i,n):
                    sb.append(s[i:j+1])
            return sb 
        re = 1
        for a in getSub(s):
            for b in getSub(t):
                c = a +b 
                if len(c)> re and c == c[::-1]:
                    re = len(c)
        return re 





re =Solution()
print(re)