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

from typing import List, Tuple, Optional

class DSU:
    def __init__(self,N):
        self.p  = list(range(N))
        self.rank = [1]*N
    
    def find(self,x):
        if self.p[x] != x:
            self.p[x] =self.find(self.p[x])
        return self.p[x]
    
    def union(self,x,y):
        xr = self.find(x)
        yr = self.find(y)
        if xr == yr:
            return
        self.p[yr] = xr
        self.rank[xr] += self.rank[yr]

    def next(self,x):
        xp = self.find(x)
        return xp + self.rank[xp] 



class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        sl=SortedList([])
        mn = nums[0]
        n = len(nums)
        if len(nums) <=1:
            return 0
        if len(nums) ==2 and nums[0] > nums[1]:
            return 1
        for i in range(1,n):
            sl.add((nums[i-1] + nums[i], i,i+2))
        pre =DSU(n+1)
        dic ={}
        cnt =0
        isG = False
        while isG ==False:
            while sl[0][1] !=0:
                                #print(sl)
                a,b,c =sl[0]
                sl.remove((a,b,c))
                if pre.next(pre.next(b)) != c:
                    continue
                nums[b]=a
                pre.union(b,pre.next(b))
                c = pre.next(b)
                sl.add((nums[b]+nums[c],b,pre.next(c)))
                cnt +=1
                if b !=0:
                    b1 = pre.find(b-1)
                    sl.add((nums[b1] + nums[b],b1,pre.next(b)))
            isG = True
            
            rm =[]
            for a,b,c in sl:
                if pre.next(pre.next(b)) !=c:
                    rm.add((a,b,c))
            for a,b,c in rm:
                sl.remove((a,b,c))
            m = len(sl)
            for i in range(1,m):
                if sl[i][1] <sl[i-1][1]:
                    isG = False
            if isG ==False:
                cnt +=1
                a,b,c = sl[0]
                sl.remove((a,b,c))
                nums[b] = a 
                pre.union(b,pre.next(b))
                b1 = pre.next(b)
                sl.add((nums[b] + nums[b1],b,pre.next(b1)))
        return cnt


re =Solution().minimumPairRemoval([2,2,-1,3,-2,2,1,1,1,0,-1])
print(re)