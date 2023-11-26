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
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m,n = len(mat),len(mat[0])
        mat1 = [list(mat[i]) for i in range(m)]
        k = k%n
        for i in range(m):
            if i%2 ==0:
                mat1[i] = mat1[i][k:] + mat1[i][:k]
            else:
                mat1[i] = mat1[i][-k:] + mat1[i][:-k]
        isG = True
        #print(mat1)
        for i in range(m):
            if tuple(mat[i]) != tuple(mat1[i]):
                isG = False
        return isG




re =Solution().areSimilar([[4,9,10,10],[9,3,8,4],[2,5,3,8],[6,1,10,4]],5)
print(re)