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

class FenwickTree:
    def __init__(self,arr) -> None:
        self.n =len(arr)
        self.bit= [0]*self.n
        for i in range(self.n):
            self.add(i,arr[i])
    
    def sumTo(self, r):
        ret = 0
        while r >=0:
            ret += self.bit[r]
            r = (r&(r+1))-1
        return ret
    
    def add(self,idx,delta):
        while idx < self.n:
            self.bit[idx] += delta
            idx =  idx | (idx +1)

class Solution:
    def minInversionCount(self, nums: List[int], k: int) -> int:
        vs = list(set(nums))
        vs.sort()
        n = len(vs)
        dic ={}
        for i,a in enumerate(vs):
            dic[a] = i 
        arr = [0]*(n+1)
        ft = FenwickTree(arr)
        m = len(nums)
        mn = m*m
        acc =0
        for i in range(m):
            if i >=k:
                t2 = dic[nums[i-k]]
                ft.add(t2,-1)
                acc -= ft.sumTo(t2-1)
            t1 = dic[nums[i]]
            acc += min(k-1,i)- ft.sumTo(t1)
            ft.add(t1,1)
            
            if i >= k-1:
                mn = min(mn,acc)
            #print(i,acc,ft.bit)
        return mn
        






re =Solution().minInversionCount(nums = [65,89,88,42,3,42,26,2,37,66], k = 9)
print(re)