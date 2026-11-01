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
    def countMagicalPairs(self, s: str) -> int:
        n = len(s)
        ans = 0
        arr = [ord(c) - ord('a') for c in s]
        poss = [[] for _ in range(26)]
        for idx, val in enumerate(arr):
            poss[val].append(idx)

        ans = 0
        for j in range(n - 1):
            pos1 = []
            for c in range(26):
                lst = poss[c]
                if not lst:
                    continue
                idx = bisect_right(lst, j) - 1
                if idx >= 0:
                    pos1.append(lst[idx])


            pos2 = []
            for c in range(26):
                lst = poss[c]
                if not lst:
                    continue
                idx = bisect_left(lst, j + 1)
                if idx < len(lst):
                    pos2.append(lst[idx])

            if not pos1 or not pos2:
                continue

            pos1.sort(reverse=True) 
            pos2.sort() 

            count1 = [0] * (len(pos1) + 1)
            for idx in range(len(pos1)):
                distinct_count = idx + 1
                if idx == 0:
                    next_p = pos1[1] if len(pos1) > 1 else -1
                    count1[distinct_count] = pos1[0] - next_p
                elif idx == len(pos1) - 1:
                    count1[distinct_count] = pos1[idx] + 1
                else:
                    count1[distinct_count] = pos1[idx] - pos1[idx + 1]

            count2 = [0] * (len(pos2) + 1)
            for idx in range(len(pos2)):
                distinct_count = idx + 1
                if idx == len(pos2) - 1:
                    count2[distinct_count] = n - pos2[idx]
                else:
                    count2[distinct_count] = pos2[idx + 1] - pos2[idx]

            max_c = min(len(pos1), len(pos2))
            for c in range(1, max_c + 1):
                if count1[c] > 0 and count2[c] > 0:
                    ans += count1[c] * count2[c]

        return ans


re =Solution().countMagicalPairs("abcac")
re =Solution().countMagicalPairs("aaa")
print(re)