from typing import List, Tuple, Optional

from collections import defaultdict, deque
from functools import cache
import heapq
from heapq import heappop, heappush
from sortedcontainers import SortedDict, SortedList

from bisect import bisect_right, insort_left, bisect_left
from queue import Queue, LifoQueue, PriorityQueue
import math

INF = math.inf


class Solution:
    def countValidSubstrings(self, s: str) -> int:
        cnt = 0
        dic = defaultdict(deque)
        l = 0

        def verify():
            cb = bisect_left(dic["b"], dic["a"][0])
            if cb >= len(dic["b"]):
                return False
            cc = bisect_left(dic["c"], dic["b"][cb])
            if cc >= len(dic["c"]):
                return False
            return True

        for i, a in enumerate(s):
            dic[a].append(i)
            while (
                len(dic["a"]) > 0
                and len(dic["b"]) > 0
                and len(dic["c"]) > 0
                and verify()
            ):
                dic[s[l]].popleft()
                l += 1
            cnt += i - l + 1
        return cnt


re = Solution()
print(re)
