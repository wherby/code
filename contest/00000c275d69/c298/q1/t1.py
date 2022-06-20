from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left
from typing import Counter

class Solution:
    def greatestLetter(self, s: str) -> str:
        c = Counter(s)
        re =""
        for i in range(26):
            k1= chr(ord('a') +i)
            k2 =chr(ord('A')+i)
            if k1 in c and k2 in c:
                re = k2 
        return re