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
            
    def queryRange(self, l, r):
        if l > r:
            return 0
        return self.sumTo(r) - self.sumTo(l - 1)

class Solution:
    def countOfPeaks(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        
        def is_peak(idx):
            if 0<idx <n-1:
                return nums[idx] > nums[idx-1] and nums[idx] > nums[idx+1]
            return False

        tree= FenwickTree([0]*n)
        treeSum= FenwickTree([0]*n)
        treesq = FenwickTree([0]*n)
        for i in range(1,n-1):
            if is_peak(i):
                tree.add(i,1)
                treeSum.add(i,i)
                treesq.add(i,i*i)

        ans = []
        for q in queries:
            if q[0] ==1:
                l,r = q[1],q[2]
                if r-l <2:
                    ans.append(0)
                else:
                    cnt = tree.queryRange(l+1,r-1)
                    sum1 = treeSum.queryRange(l+1,r-1)
                    sum2 = treesq.queryRange(l+1,r-1)
                    ret = r * sum1 + l * sum1 - sum2  - l*r *cnt
                    ans.append(ret)
            else:
                idx,val =q[1],q[2]
                if nums[idx] == val:
                    continue
                
                for i in range(max(1,idx-1),min(n-1,idx+2)):
                    if is_peak(i):
                        tree.add(i,-1)
                        treeSum.add(i,-i)
                        treesq.add(i,-i*i)
                nums[idx] = val
                for i in range(max(1,idx-1),min(n-1,idx+2)):
                    if is_peak(i):
                        tree.add(i,1)
                        treeSum.add(i,i)
                        treesq.add(i,i*i)
        return ans




re =Solution().countOfPeaks( nums = [7,15,0,11,5], queries = [[2,1,9],[1,0,4]])
print(re)