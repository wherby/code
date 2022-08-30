from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left
from functools import cache

class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        n = len(blocks)
        ls =[0]*(n+1) 
        for i,a in enumerate(blocks):
            if a == "B":
                ls[i+1] =ls[i]+1
            else:
                ls[i+1] =ls[i]
        mn = k 
        for i in range(n-k+1):
            t = k-(ls[i+k]- ls[i] )
            mn = min(mn,t)
        return mn




re =Solution().minimumRecolors(blocks = "WBBWWBBWBW", k = 7)
print(re)