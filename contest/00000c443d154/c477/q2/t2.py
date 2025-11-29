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
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        dic1 = {}
        dic1[(0,0)] =  -1 
        mx = 0 
        acc=acc2 = 0
        for i,a in enumerate(nums):
            if a %2 ==1:
                acc+=1
            else:
                acc -=1
            acc2 =acc2^a 
            if(acc,acc2) in dic1:
                mx = max(mx,i-dic1[(acc,acc2)])
            else:
                dic1[(acc,acc2)] = i 
        return mx





re =Solution()
print(re)