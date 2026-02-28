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
    def scoreDifference(self, nums: List[int]) -> int:
        f= [0,0]
        cur = 0
        for i,a in enumerate(nums,1):
            if a%2==1 :
                cur= (cur +1)%2 
            if i%6==0:
                cur = (cur +1)%2
            f[cur] +=a
            #print(i,a,cur,f)
        return f[0]-f[1]





re =Solution().scoreDifference([2,4,2,1,2,1])
print(re)