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
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        m = len(queries)
        l,r= 1,m 
        if all(a==0 for a in nums ):
            return 0
        def search(nums,tar):

            vis = [0]*(tar+1)
            vis[0] =1
            for a in nums:
                for j in range(tar,0,-1):
                    if j-a >=0 and vis[j-a] ==1:
                        vis[j] =1
            return vis[-1]==1


        def verify(mid):
            n = len(nums)
            lss= [[] for _ in range(n)]
            for a,b,c in queries[:mid]:
                for j in range(a,b+1):
                    lss[j].append(c)
            
            return all(search(lss[i],nums[i]) for i in range(n))

        while l<r:
            mid = (l+r)>>1
            if verify(mid):
                r = mid 
            else:
                l= mid +1
        return l if verify(l) else -1



re =Solution().minZeroArray( nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]])
print(re)