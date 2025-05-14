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
    def maxScore(self, n: int, edges: List[List[int]]) -> int:
        w = [14, 17, 13, 11, 12, 7, 16, 10, 5, 18, 2, 1, 20, 4, 9, 8, 15, 6, 19, 3]
        print(set(w) == set(range(1, 21)))
        print(len(w))
        ans = 0
        for u, v in edges:
            ans += w[u] * w[v]
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxScore(20,
                     [[18, 14], [12, 18], [12, 9], [1, 9], [7, 1], [5, 7], [0, 13], [6, 0], [6, 16], [15, 16], [10, 19],
                      [17, 4], [2, 4], [2, 3], [3, 8]]))

