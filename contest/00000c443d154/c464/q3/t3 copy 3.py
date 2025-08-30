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
from collections import defaultdict,deque



class DSU:
    def __init__(self,N):
        self.p  = list(range(N))
        self.rank = [1]*N
    
    def find(self,x):
        if self.p[x] != x:
            self.p[x] =self.find(self.p[x])
        return self.p[x]

    def union(self,x,y):
        self.p[self.find(x)] =self.find(y)
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        rst= deque([])
        ridx = [i for i in range(n)]
        mx = nums[0]
        ret = [0]*n 
        for i in range(n):
            mx = max(nums[i],mx)
            ret[i] =mx
        dsu = DSU(n)
        for i in range(n-1,-1,-1):
            if len(rst) ==0:
                rst.append(i)
            elif nums[rst[0]]> nums[i]:
                rst.appendleft(i)
            kidx = bisect_left(rst,max(nums[i],ret[i]),key=lambda x: nums[x])
            # if kidx< len(rst):
            #     print(nums[i],rst,kidx,i,nums[rst[kidx]],rst[kidx])
            if kidx >0:
                #ridx[i] = rst[kidx-1]
                dsu.union(i,rst[kidx-1])
        #print(ridx)
        pre = [0]*n 
        for i,a in enumerate(nums):
            pre[i] = max(pre[i-1],a)
        
        for i,a in enumerate(nums):
            ret[i] = max(a,pre[dsu.find(i)],ret[i])
        return ret




re =Solution().maxValue([9,30,16,6,36,9])
print(re)