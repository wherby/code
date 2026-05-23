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


class SparseTable:
    __slots__ = 'op', 'st'
    def __init__(self, nums, op):
        # op 需要满足可重复贡献，即 x op x = x，如 max, min, gcd, lcm, and, or
        # 建立 O(nlogn)，查询 O(1)
        n = len(nums)
        m = n.bit_length()
        st = [[0] * (n - (1<<b) + 1) for b in range(m)]
        for i, x in enumerate(nums):
            st[0][i] = x
        for b in range(1, m):
            l = 1 << (b-1)
            for i in range(n - (1<<b) + 1):
                st[b][i] = op(st[b-1][i], st[b-1][i+l])
        self.op = op
        self.st = st

    def query(self, left, right):
        b = (right - left + 1).bit_length() - 1
        return self.op(self.st[b][left], self.st[b][right - (1<<b) + 1])

class Solution:
    def countLocalMaximums(self, matrix: List[List[int]]) -> int:
        n,m = len(matrix),len(matrix[0])

        K = int(math.log2(m)) + 1
        stt = [SparseTable(arr,max) for arr in matrix]

        cnt = 0
        
        for row in range(n):
            for col in range(m):
                x = matrix[row][col]    
                if x == 0:
                    continue
                is_good = True
                r_start = max(0, row - x)
                r_end = min(n - 1, row + x)         
                for r in range(r_start, r_end + 1):
                    c_start = max(0, col - x)
                    c_end = min(m - 1, col + x)      
                    if abs(r - row) == x:
                        c_start = max(0, col - x + 1)
                        c_end = min(m - 1, col + x - 1)
                    if c_start > c_end:
                        continue
                    if stt[r].query(c_start,c_end) > x:
                        is_good = False
                        break
                if is_good:
                    cnt += 1 
        return cnt





re =Solution().countLocalMaximums( matrix = [[1,2],[3,4]])
print(re)