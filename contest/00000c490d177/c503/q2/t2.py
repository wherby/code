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
import string
class Solution:
    def passwordStrength(self, password: str) -> int:
        password = set([a for a in password])
        small_letters = set(map(chr, range(ord('a'), ord('z')+1)))
        big_letters = set(map(chr, range(ord('A'), ord('Z')+1)))
        digits = set(map(chr, range(ord('0'), ord('9')+1)))
        other = "!@#$"
        other =set([a for a in other])
        cnt = 0
        for a in password:
            if a in small_letters:
                cnt +=1
            elif a in big_letters:
                cnt +=2
            elif a in digits:
                cnt +=3
            elif a in other:
                cnt +=5
        return cnt




re =Solution().passwordStrength("vqztn2Z")
print(re)