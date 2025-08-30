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
from itertools import pairwise

    # a,b,c 
    # b >c 
    # a> b 

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
        ret = [0]*n
        st =[]
        dsu = DSU(n)
        for i,a in enumerate(nums):
            while st and a >= nums[st[-1]]:
                b = st.pop()
                if nums[b] < a:
                    dsu.union(b,i)
            if st:
                dsu.union(i,st[-1])
            st.append(i)
        #print(st)
        while len(st)>1:
            b = st.pop()
            dsu.union(b,st[0])
        for i in range(n):
            ret[i] =nums[dsu.find(i)]
        return ret



re =Solution().maxValue([30,21,5,35,24])
print(re)