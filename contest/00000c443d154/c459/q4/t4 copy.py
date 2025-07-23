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


from collections import defaultdict
from math import gcd

MOD = 10**9 + 7

from collections import defaultdict
from math import gcd

MOD = 10**9 + 7


def get_slope(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    if dx == 0 and dy == 0:
        return (0, 0)
    if dx == 0:
        return (1, 0)  # vertical line
    if dy == 0:
        return (0, 1)  # horizontal line
    g = math.gcd(dy, dx)
    dy //= g
    dx //= g
    if dx < 0:
        dy *= -1
        dx *= -1
    return (dy, dx)

def are_collinear(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) == (p3[0] - p1[0]) * (p2[1] - p1[1])
class Solution:




    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 4:
            return 0


        slope_groups = defaultdict(list)

        for i in range(n):
            for j in range(i + 1, n):
                slope = get_slope(points[i], points[j])
                slope_groups[slope].append((i, j))

        unique_trapezoids = set()

        for slope in slope_groups:
            edges = slope_groups[slope]
            if len(edges) < 2: 
                continue

            for i in range(len(edges)):
                for j in range(i + 1, len(edges)):
                    idx1, idx2 = edges[i]
                    idx3, idx4 = edges[j]

                    p1, p2 = points[idx1], points[idx2]
                    p3, p4 = points[idx3], points[idx4]


                    all_indices = {idx1, idx2, idx3, idx4}
                    if len(all_indices) != 4:
                        continue 

                    if (are_collinear(p1, p2, p3) or
                        are_collinear(p1, p2, p4) or
                        are_collinear(p1, p3, p4) or
                        are_collinear(p2, p3, p4)):
                        continue
                    trapezoid_key = tuple(sorted(list(all_indices)))
                    unique_trapezoids.add(trapezoid_key)

        return len(unique_trapezoids)



re =Solution().countTrapezoids([[82,7],[82,-9],[82,-52],[82,78]])
print(re)