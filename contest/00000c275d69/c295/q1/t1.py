from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left
from typing import Counter

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        c =Counter(s)
        c2 = Counter(target)
        mx = len(s)
        for k,v in c2.items():
            v2 =c.get(k,0)
            mx = min(mx, v2//v)
        return mx