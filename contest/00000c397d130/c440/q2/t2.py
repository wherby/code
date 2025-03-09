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
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        ls= [(a,i) for i,a in enumerate(nums1)]
        ls.sort()
        n = len(nums1)
        ret = [0]*n
        lstv  = ls[0][0]
        sl = SortedList()
        pre = [0]*n
        acc = 0
        for idx,(a,i) in enumerate(ls):
            pre.append(pre[-1] +nums2[i])
            dic[a] +=1
            ret[i] = pre[-dic[a]-1]- pre[-dic[a]-1 -k-1]
            print(pre,dic[a],a,i)
        return ret
            




re =Solution().findMaxSum(nums1 = [4,2,1,5,3], nums2 = [10,20,30,40,50], k = 2)
print(re)