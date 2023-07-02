from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        for i in range(n):
            for j in range(i+1,n):
                a = int(str(nums[i])[0])
                b = int(str(nums[j])[-1])
                if math.gcd(a,b) ==1:
                    cnt +=1
                    #print(i,j)
        return cnt





re =Solution().countBeautifulPairs([31,25,72,79,74])
print(re)