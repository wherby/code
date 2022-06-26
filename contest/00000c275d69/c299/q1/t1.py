from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution(object):
    def checkXMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        n = len(grid)
        def isEdg(x,y):
            if x ==y or x +y ==n-1:
                return True
            else:
                return False
        for i in range(n):
            for j in range(n):
                if isEdg(i,j) and grid[i][j] ==0:
                    #print(i,j)
                    return False
                elif isEdg(i,j)==False and grid[i][j] !=0:
                    #print(i,j)
                    return False
        return True
    
re =Solution().checkXMatrix([[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]])
print(re)