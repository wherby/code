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
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        state = [tuple(nums1)]
        n = len(nums1)
        visit = {}
        if nums1 == nums2:
            return 0
        nums2 = tuple(nums2) 
        def getNext(ls):
            #ls = list(ls)
            tmp= []
            for l in range(1,n+1):
                for i in range(l,n):
                    ls1 =ls[i-l:i]
                    ls2 = ls[:i-l]+ls[i:]
                    m = len(ls2)
                    for k in range(m+1):
                        ls3 = ls2[:k]+ls1 + (ls2[k:] if k !=m else ())
                        ls3 = tuple(ls3)
                        if ls3 not in visit:
                            tmp.append(ls3)
            return tmp
        acc = 0
        while state:
            tmp = set([])
            for a in state:
                #print(a)
                if a in visit:continue
                if a == nums2:
                    return acc 
                for b in getNext(a):
                    tmp.add(b)
                visit[a] = 1
            acc +=1
            state = tmp 
        #print(visit)
        





re =Solution().minSplitMerge( nums1 = [1,1,2,3,4,5], nums2 = [5,4,3,2,1,1])
print(re)