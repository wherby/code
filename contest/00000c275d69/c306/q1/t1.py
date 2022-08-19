from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left
from functools import cache

class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        m,n = len(grid),len(grid[0])
        res =[[0]*(n-2) for _ in range(m-2)]
        for i in range(m-2):
            for j in range(n-2):
                res[i][j] = max([grid[i+x][j+y] for x in range(3) for y in range(3)])
        return res
                





re =Solution().largestLocal( [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]])
print(re)