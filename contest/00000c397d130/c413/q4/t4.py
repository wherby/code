from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math

from math import inf

class node:
    def __init__(self) -> None:
        self.child ={}
        self.mx =-inf
        self.is_end = -1

class Trie:
    def __init__(self) -> None:
        self.root = node()
    
    def insert(self,w,idx):
        ls = '{:032b}'.format(w)
        r = self.root
        for i in ls:
            i = int(i)
            if i not in r.child:
                r.child[i] = node()
            r = r.child[i]
            r.mx= idx
        r.is_end = w
    
    def get(self,x,idx):
        r =self.root
        if len(r.child) == 0:
            return -1
        ls = '{:032b}'.format(x)
        for i in ls:
            i = int(i)
            if i not in r.child and r.mx <idx:
                r= r.child[1-i]
            else:
                r = r.child[i]
        return r.is_end
    

class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        lss = [[] for _ in range(n)]
        m = len(queries)
        qs = [[] for _ in range(n)]
        for i,(a,b) in enumerate(queries):
            qs[b].append((i,a))
        for i,a in enumerate(nums):
            for j in range(i):
                tmp = list(lss[j])
                for b in lss[j]:
                    tmp.append(a^b)
                lss[j]= tmp
            lss[i].append(a)
            








re =Solution().maximumSubarrayXor(nums = [2,8,4,32,16,1], queries = [[0,2],[1,4],[0,5]])
print(re)