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

P= 4194301
class StringHash:
    def __init__(self,s1):
        n =len(s1)
        self.hls =[0]*(n+1)
        self.pls =[1]*(n+1)
        self.mod = 2<<64
        for i in range(n):
            self.hls[i+1] = (self.hls[i]*P +s1[i])%self.mod
            self.pls[i+1] = (self.pls[i]*P)%self.mod
    
    def query(self,left,right):
        return (self.hls[right]- (self.hls[left]*self.pls[right-left]) % self.mod) % self.mod

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        l,r = 1,len(nums)
        sth = StringHash(nums)
        def verify(md):
            dic = defaultdict(int)
            for r in range(md,len(nums)+1):
                t = sth.query(r-md,r)
                dic[t] +=1
            for k,v in dic.items():
                if v == 1:
                    return True
            return False

        while l<r:
            md = (l+r)>>1
            if verify(md):
                r=md 
            else:
                l = md+1
        return l








re =Solution().smallestUniqueSubarray([2,1,2,3,3])
print(re)