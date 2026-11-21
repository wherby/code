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
    def canRemoveAll(
        self, types: list[int], colors: list[int], groupSize: list[int]
    ) -> bool:
        st = []
        dic = {i: a for i, a in enumerate(groupSize)}
        for t, c in zip(types, colors):
            if st and st[-1][0] == t and st[-1][1] == c:
                t1, c1, cnt1 = st.pop()
                st.append((t1, c1, cnt1 + 1))
                if cnt1 + 1 == dic[t1]:
                    st.pop()
            else:
                st.append((t, c, 1))
                if 1 == dic[t]:
                    st.pop()
        return len(st) == 0


re = Solution().canRemoveAll(types=[0, 1, 1, 0], colors=[5, 3, 3, 5], groupSize=[2, 2])
print(re)
