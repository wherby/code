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


from collections import defaultdict, deque
from bisect import bisect_left


class Solution:
    def countValidSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = 0
        l = 0

        for i in range(n):

            if i >= 2 and s[i - 2] == "a" and s[i - 1] == "b" and s[i] == "c":
                l = max(l, i - 1)
            cnt += i - l + 1

        return cnt


# 测试
re = Solution().countValidSubstrings("abac")
print(re)  # 输出对应的正确不包含 "abc" 的子串数量
