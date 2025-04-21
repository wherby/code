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
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        nums = [a%k for a in nums]
        ret = [0]*k
        ans = [0]*k
        for a in nums:
            tmp=[0]*k
            for i,b in enumerate(ret):
                c = i*a%k
                tmp[c] +=b
                #tmp[i] +=b
            tmp[a] +=1
            for i,b in enumerate(tmp):
                ans[i]+=b
            ret =list(tmp)
            #print(a,tmp,ans)
        return ans




re =Solution().resultArray(nums = [1,2,3,4,5], k = 3)
print(re)