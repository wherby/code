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
    def countSubarrays(self, nums: list[int], k: int, m: int) -> int:
        n =len(nums)
        ans = 0

        c = defaultdict(int)
        kn = 0 
        l = 0
        l2 =0
        for i in range(n):
            c[nums[i]]+=1       
            if c[nums[i]]==m:
                kn+=1

            
            
            while len(c)>k:
                c[nums[l]]-=1
                if c[nums[l]]==m-1:
                    kn-=1
                if c[nums[l]]==0:
                    del c[nums[l]]
                l+=1
                if l2<l:
                    l2=l
            while l2<i:
                if c[nums[l2]]>m:
                    c[nums[l2]]-=1
                    l2+=1
                else:
                    break
            if kn==k and len(c)==k:
                ans+=l2-l+1
            l = l2
        return ans
            





re =Solution().countSubarrays( nums = [1,2,1,2,2], k = 2, m = 2)
print(re)