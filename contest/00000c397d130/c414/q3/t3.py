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
    def findMaximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        st =[]
        acc=0
        for i,a in enumerate(nums):
            if st and nums[st[-1]] >= a :
                continue
            while len(st)>0 and a >nums[st[-1]]:
                c= st.pop()
                acc += nums[c] * (i-c)
               # print(acc)
            st.append(i)
        acc += nums[st[-1]] *(n-1-st[-1])
        #print(st[-1])
        return acc




re =Solution().findMaximumScore([1,3,1,5])
print(re)