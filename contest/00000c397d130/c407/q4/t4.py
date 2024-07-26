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
from itertools import pairwise

class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        ls = [a-b for a,b in zip(nums,target)]
        #ls = [a-b for a,b in pairwise(ls)]
        state = []
        #print(ls)
        for a in ls:
            if len(state)==0 and a ==0: continue
            
            if len(state) and a == state[-1]:
                continue
            
            if len(state) ==0:
                state.append(a)
            elif len(state) ==1:
                state.append(a)
            else:
                while len(state)>=2 and (a-state[-1]) *(state[-1]-state[-2]) >0:
                    state.pop()
                state.append(a)
        sm = 0
        #print(state)
        for a in state:
            sm += abs(a)
        n = len(state)
        for i in range(n-1):
            if state[i] * state[i+1] >=0:
                sm -= min(abs(state[i]), abs(state[i+1]))
        return sm
        




re =Solution().minimumOperations( nums = [9,2,6,10,4,8,3,4,2,3], target = [9,5,5,1,7,9,8,7,6,5])
print(re)

# [0, -3, 1, 9, -3, -1, -5, -3, -4, -2]
# [0, -3, 9, -3, -1, -5, -3, -4, -2]
#         12      14 16   