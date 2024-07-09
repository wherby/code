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
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pls= [[0]*32 for _ in range(n+1)]
        for i,a in enumerate(nums):
            for j in range(32):
                if (1<<j)&a:
                    pls[i+1][j] =pls[i][j]+1
                else:
                    pls[i+1][j] =pls[i][j]
        sm =0
        @cache
        def get(s,e):
            tmp= 0
            for i in range(32):
                if pls[e+1][i]-pls[s][i] == e-s+1:
                    tmp+= 1<<i
            return tmp
        for i in range(n):
            l,r = i,n-1
            while l<r:
                mid = (l+r)>>1
                if get(i,mid)>k:
                    l = mid+1
                else:
                    r = mid
                #print("1")
            #print(get(i,mid),k,i,mid,"a")
            if get(i,l) != k :
                continue
            ll = l
            l,r = mid,n-1
            #print(l,r)
            while l <r:
                mid = (l+r+1)>>1
                #print(l,r,mid,'c')
                if get(i,mid)<k:
                    r= mid-1
                else:
                    l = mid
                #print(l,r,get(i,mid),mid,sm)
            sm += l-ll+1
            #print(i,sm,mid,ll,get(i,mid) ,"n")
        return sm
                    





re =Solution().countSubarrays(nums = [1,0,10,10,4], k = 4)
print(re)