# common include
from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

from itertools import chain,product
from collections import Counter

class Solution(object):
    def containsPattern(self, arr, m, k):
        """
        :type arr: List[int]
        :type m: int
        :type k: int
        :rtype: bool
        """
        n =len(arr)
        t = m*k
        for i in range(n-t+1):
            cans = arr[i:i+t]
            a1 =arr[i:i+m]
            a1t =tuple(a1)
            fd = True
            for j in range(k):
                a2=arr[i+m*j : i+m*j+m]
                a2t =tuple(a2)
                if a1t !=a2t:
                    fd =False
            if fd == True:
                return True
        return False

re =Solution().containsPattern(arr =[1,2,4,4,4,4], m = 1, k = 3)
print(re)