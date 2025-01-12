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
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = [0]
        for a in nums:
            pre.append(pre[-1] +a)
        st =deque([])
        acc = 0
        cnt =0
        for i,a in enumerate(nums):
            while len(st) and nums[st[-1]] <a:
                st.pop()
            if len(st)>0:
                acc += st[0] - a 
            st.append(i)
            while acc> k and len(st)>1:
                cnt +=n -i
                b = st[0]-st[1]
                






re =Solution()
print(re)