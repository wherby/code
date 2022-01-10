from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix)
        def verify(tls):
            tls.sort()
        
            for j in range(n):
                if tls[j] != j+1:

                    return False
            return True
        for i in range(n):
            tls = list(matrix[i])
            t2ls =[]
            for j in range(n):
                t2ls.append(matrix[j][i])
            if verify(tls) and verify(t2ls):
                continue
            else:
                ##print(verify(tls) , verify(t2ls))
                return False
        return True

re = Solution().checkValid(matrix = [[1,1,1],[1,2,3],[1,2,3]])
print(re)
            
            