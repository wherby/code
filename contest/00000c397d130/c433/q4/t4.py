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
    def minMaxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def getMN(nums):
            pre,pst= [max(-1,i-k) for i in range(n)],[min(i+k,n ) for i in range(n)]
            st= deque([])
            
            for i,a in enumerate(nums):
                while st and i-st[0] >=k:
                    st.popleft()
                while st and nums[st[-1]] >a:
                    b = st.pop()
                    pst[b] = i 
                st.append(i)
            st= deque([])
            for i in range(n-1,-1,-1):
                while st and st[0] -i >=k:
                    st.popleft()
                while st and nums[st[-1]]>nums[i]:
                    b = st.pop()
                    pre[b] = i
                st.append(i)
                #print(st,pre)
            acc =0
            for i,a in enumerate(nums):
                acc += a*(i- pre[i]) *(pst[i]-i) //2 
            return acc  
        a = getMN(nums)
        b = getMN([-a for a in nums])
        print(a,b)
        return a -b





re =Solution().minMaxSubarraySum(nums = [1,2,3], k = 2)
print(re)