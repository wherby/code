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
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        ls =[0]*(n+1)
        dic = defaultdict(list)
        for a,b in queries:
            ls[a] +=1
            ls[b+1] -=1
            dic[a].append(b)
        acc =0
        
        for i,a in enumerate(nums):
            acc += ls[i]
            #print(i,a,acc)
            if acc < a:
                #print("a",i,acc,a)
                return -1
        ls = [0]*(n+1)
        st = []
        acc =0
        ret = 0
        for i,a in enumerate(nums):
            acc += ls[i]
            for b in dic[i]:
                heappush(st,-b)
            #print(st,i,a)
            while acc<a:
                #print(a,st,i,)
                b = heappop(st)
                if -b>=i:
                    acc +=1
                    ls[-b+1]-=1
                else:
                    ret +=1
            #print(st,i,a,ls)
        return len(st)+ret






re =Solution().maxRemoval(nums = [1,1,1,1], queries = [[1,3],[0,2],[1,3],[1,2]])
print(re)
# re  =Solution().maxRemoval([1,2,3,4], queries = [[0,3]])
# print(re)