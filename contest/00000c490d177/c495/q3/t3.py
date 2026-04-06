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
from collections import Counter



class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n =len(nums)
        ans = 0
        sortedLs= sorted(nums)
        def check(k):
            for i in range(0,n,k):
                sub = nums[i:i+k]
                tar = sortedLs[i:i+k]
                if Counter(sub) != Counter(tar):
                    return False
                d_c = 0
                for i in range(k-1):
                    if sub[i]>sub[i+1]:
                        if sub[i] == tar[-1] and sub[i+1] == tar[0] and sub[-1]<=sub[0]:
                            d_c +=1
                        else:
                            return False
                if d_c>1:
                    return False
            return True
                

        for i in range(1,n+1):
            if n%i == 0:
                if check(i):
                    ans +=i 
        return ans 







re =Solution()
print(re)