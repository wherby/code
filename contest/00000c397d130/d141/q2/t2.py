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
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        n  = len(nums)

        ret = [-1] *n 
        for i in range(n):
            a = nums[i]
            if a %2 ==0:
                continue
            b = bin(a)[2:]
            m = len(b)
            for j in range(m-1,-1,-1):
                if b[j]!="1":
                    break
            if j == 0:
                ret[i] = a //2 
            else:
                s = b[:j+1]+ "0"+ "1"*(m-j-2)
                #print(s,b[:j+1],(m-j-2),j,a,b)
                ret[i] = int(s,2)
        return ret







re =Solution().minBitwiseArray([11,13,31])
print(re)