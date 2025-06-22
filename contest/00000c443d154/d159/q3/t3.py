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

def primeUpTo(n):
    primes = set(range(2,n+1))
    for i in range(2,n):
        if i in primes:
            it = i*2
            while it <=n:
                if it in primes:
                    primes.remove(it)
                it +=i 
    return primes

class Solution:
    def primeSubarray(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        ps = primeUpTo(mx)
        acc = 0
        l = 0
        sl = SortedList([])
        st = deque([])
        for i,a in enumerate(nums):
            if a in ps:
                sl.add(a)
                st.append(i)
            while len(sl) and  sl[-1] - sl[0]>k:
                if nums[l] in ps:
                    sl.remove(nums[l])
                    st.popleft()
                l +=1
            if len(st)>=2:
                acc += st[-2]-l+1
            #print(sl,st,i,a,l)
        return acc



re =Solution().primeSubarray(nums = [2,3,5,7], k = 3)
print(re)