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
    def maxSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        dic = defaultdict(int)
        l =0 
        acc = 0
        
        for r in range(n):
            a = nums[r]
            for b in list(dic.keys()):
                c = a-b 
                if c in dic:
                    if b < c :
                        acc += dic[b] * dic[c]
                    elif b ==c:
                        acc += dic[b] *(dic[b] -1) //2 
            
            for b in list(dic.keys()):
                c = b -a 
                if c in dic :
                    acc += dic[b] * dic[c]
            dic[a] +=1
            while acc >0 :
                d = nums[l]
                
                dic[d] -=1
                for b in list(dic.keys()):
                    c = d -b 
                    if c in dic:
                        if b < c :
                            acc  -= dic[b]*dic[c]
                        elif b ==c:
                            acc -= dic[b] *(dic[b] -1)//2 
                for b in list(dic.keys()):
                    c = b- d 
                    if c in dic :
                        acc -= dic[d] * dic[c]
                
                if dic[d] ==0:
                    del dic[d]
                l +=1
            ans = max(ans,r-l +1)
        return ans




re =Solution().maxSubarray( [2,3,5,3,2,1])
print(re)