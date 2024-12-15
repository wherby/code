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



class StringHash:
    def __init__(self,s1):
        n =len(s1)
        self.hls =[0]*(n+1)
        self.pls =[1]*(n+1)
        self.mod = 2<<64
        for i in range(n):
            self.hls[i+1] = (self.hls[i]*131 +s1[i])%self.mod
            self.pls[i+1] = (self.pls[i]*131)%self.mod
    
    def query(self,left,right):
        return (self.hls[right]- (self.hls[left]*self.pls[right-left]) % self.mod) % self.mod

class Solution:
    def beautifulSplits(self, nums: List[int]) -> int:
        hs = StringHash(nums)
        n = len(nums)
        cnt =0
        for i in range(1,n):
            isG1 = False
            if (i)*2<n:
                if hs.query(0,i) == hs.query(i,(i)*2):
                    isG1 =True
                    cnt += n-i*2
                    print(isG1,cnt,i,hs.query(0,i),hs.query(i,(i)*2))
            if isG1 == False:
                for j in range(i+1,n):
                    if (j-i)*2 > n-i:continue
                    if hs.query(i,j) ==hs.query(j,j+j-i):
                        cnt += 1
                        print(i,j,n)
        return cnt




# re =Solution().beautifulSplits(nums = [3,3,3,1,3])
# print(re,3)
re =Solution().beautifulSplits(nums = [0,0,0,0,2,2,0,1,2,1,2])
print(re,19)