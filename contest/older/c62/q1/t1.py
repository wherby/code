from collections import defaultdict
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        cnt = len(original)
        if cnt != m*n:
            return []
        res = []
        for i in range(m):
            tp =[]
            for j in range(n):
                tp.append(original[i*n +j])
            res.append(tp)
        return res


Solution().construct2DArray([1,2,3,4],2,2)