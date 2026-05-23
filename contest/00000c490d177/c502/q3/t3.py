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
    def countLocalMaximums(self, matrix: List[List[int]]) -> int:
        n,m = len(matrix),len(matrix[0])

        K = int(math.log2(m)) + 1
        st = [[[0] * m for _ in range(K)] for _ in range(n)]
        
        for r in range(n):
            for c in range(m):
                st[r][0][c] = matrix[r][c]
                
            for k in range(1, K):
                length = 1 << (k - 1)
                for c in range(m - (1 << k) + 1):
                    st[r][k][c] = max(st[r][k - 1][c], st[r][k - 1][c + length])
                    
        def query_row_max(r, c_start, c_end):
            if c_start > c_end:
                return -1
            k = int(math.log2(c_end - c_start + 1))
            return max(st[r][k][c_start], st[r][k][c_end - (1 << k) + 1])

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
                        if col - x >= 0:
                            c_start = col - x + 1  
                        if col + x < m:
                            c_end = col + x - 1   
                    if c_start > c_end:
                        continue
                    if query_row_max(r, c_start, c_end) > x:
                        is_good = False
                        break
                if is_good:
                    cnt += 1 
        return cnt




re =Solution().countLocalMaximums( matrix = [[1,2],[3,4]])
print(re)