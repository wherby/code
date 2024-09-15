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
    def maxValue(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)
        cand = [i for i in nums]
        for i in range(6,-1,-1):
            ret =[]
            for j in range(n):
                if (1<<i)& nums[j]:
                    ret.append(j)
            tmp =set(cand) & set(ret)
            tmp = sorted(list(tmp))
            
            if len(tmp)>=k and (tmp[k-1]<n-k or tmp[-k]>=k) and len(tmp)!=n:
                #print(tmp,cand,i)
                res += 1<<i
                cand = tmp 
        return res




re =Solution().maxValue(nums = [2,6,7], k = 1)
print(re)