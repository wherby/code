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
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        left = [-1]*n
        right = [n] *n 
        st = [] 
        for i,a in enumerate(nums):
            while st and nums[st[-1]]>= a :
                st.pop()
            if st:
                left[i] = st[-1]
            st.append(i)
        st =[]
        for i in range(n-1,-1,-1):
            while st and nums[st[-1]] >= nums[i]:
                st.pop()
            if st:
                right[i] = st[-1]
            st.append(i)
        dp = [True]*n 
        for i in range(n):
            if left[i] != i-1:
                dp[i] = False
        for i in range(n-1,-1,-1):
            if right[i] != i +1:
                dp[i] = False
        sm= sum(nums)
        ret = sm +1
        acc =0
        print(dp)
        for i in range(n):
            if dp[i]:
                ret = min(ret,abs(sm-acc*2))
            acc += nums[i]
            if dp[i]:
                ret = min(ret,abs(sm-acc*2))
        return ret if ret <=sm else -1





re =Solution().splitArray([3,1,2])
print(re)