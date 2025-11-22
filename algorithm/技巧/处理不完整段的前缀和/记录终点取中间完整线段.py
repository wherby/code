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
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n= len(nums)
        ls = [-1]
        for i in range(n):
            if i >0 and nums[i]< nums[i-1]:
                ls.append(i-1)
        ls.append(n-1)
        pls = [0]
        for a,b in pairwise(ls):
            pls.append(pls[-1] + (b-a) *(b-a+1)//2)
        ret = []
        for l, r in queries:
            k_s = bisect_left(ls, l) 
            k_e = bisect_left(ls, r) - 1
            if k_s > k_e:
                d = r-l +1
                ret.append( d*(d+1)//2)
                continue
            cnt = pls[k_e] - pls[k_s]
            d1 = ls[k_s] -l +1 
            cnt += d1*(d1+1)//2 
            d2 = r -ls[k_e]  
            cnt += d2*(d2+1)//2
            #print(d1,d2,cnt)
            ret.append(cnt)
        return ret





re =Solution().countStableSubarrays(nums = [3,4,2], queries = [[1,2]])
print(re)