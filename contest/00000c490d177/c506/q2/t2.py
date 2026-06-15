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
from collections import Counter

class MaxFreq():
    def __init__(self):
        self.mx = 0
        self.fdict = defaultdict(set)
        self.dic = defaultdict(int)
    
    def add(self,a):
        if self.dic[a] !=0:
            self.fdict[self.dic[a]].remove(a)
            if len(self.fdict[self.dic[a]]) ==0:
                del self.fdict[self.dic[a]]
        self.dic[a] +=1
        self.fdict[self.dic[a]].add(a)
        self.mx = max(self.mx,self.dic[a])
    
    def remove(self,a):
        self.fdict[self.dic[a]].remove(a)
        if len(self.fdict[self.dic[a]]) == 0 and self.mx ==self.dic[a]:
            self.mx -=1
        self.dic[a] -=1
        self.fdict[a].add(a)
     

class Solution:
    def getLength(self, nums: List[int]) -> int:
        n = len(nums)
        ret = 1 
        for i in range(n):
            c = MaxFreq()
            mxk =0
            for j in range(i,n):
                c.add(nums[j])
                isG = True
                if len(c.dic.keys())>1:
                    ks = list(c.fdict.keys())
                    ks.sort()
                    if len(ks) != 2 or ks[0] *2 != ks[1]:
                        isG = False
                if isG:
                    ret = max(ret,j-i+1)
        return ret

                




re =Solution().getLength(nums = [1,2,2,1,2,3,3,3])
print(re)