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
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        dic = defaultdict(list)
        for i,a in enumerate(nums):
            dic[a].append(i)
        n = len(nums)
        for k,v in dic.items():
            v1 = [-n+ v[-1]] + v + [v[0] +n]
            dic[k] =v1
        ret =[-1]*len(queries)
        
        for i,a in enumerate(queries):
            k = bisect_left(dic[nums[a]],a)
            if len(dic[nums[a]]) ==3:
                continue
            re = 10**6
            #print(a,k,dic[nums[a]])

            re =min(re,dic[nums[a]][k+1]-a, n-(dic[nums[a]][k+1]-a))


            re=  min(re,a-dic[nums[a]][k-1],n-(a-dic[nums[a]][k-1]))
            ret[i] = re
        return ret




re =Solution().solveQueries( nums = [14,14,4,2,19,19,14,19,14], queries = [2,4,8,6,3])
print(re)