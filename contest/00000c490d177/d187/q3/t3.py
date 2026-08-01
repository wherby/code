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
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        mod = 10**9+7 
        c1 = len([x for x in nums if x <a ])
        c2 = len([x for x in nums if x > b ])
        n = len(nums)
        idx1 = 0 
        idx2 = c1
        idx3 = n -c2 
        acc = 0 
        ret = []
        for i,x in enumerate(nums):
            if x<a :
                ret.append(idx1)
                idx1 +=1 
            elif x>b:
                ret.append(idx3)
                idx3+=1
            else:
                ret.append(idx2)
                idx2 +=1 
        sl = SortedList()
        print(ret)
        for i,a in enumerate(ret):
            t= sl.bisect_left(a)
            acc += i-t
            sl.add(a)
            #print(t,i,acc,a)
        return acc %mod
                




re =Solution().minAdjacentSwaps(nums = [1,3,2,4,5,6], a = 3, b = 4)
print(re)