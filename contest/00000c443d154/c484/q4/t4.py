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
    def maximumAND(self, nums: List[int], k: int, m: int) -> int:
        ret = 0 

        for l in range(32,-1,-1):
            st = []
            msk = 1<<l
            for i,a in enumerate(nums):
                if a & msk:
                    heappush(st,(0,i))
                else:
                    c = msk- a%msk 
                    if a > msk:
                        c = min(c,a%msk +1)
                    heappush(st,(c,i))
            acc = 0 
            cand =[]
            if l ==2:
                print(st)
            for _ in range(m):
                cost,idx = heappop(st)
                cand.append([cost,idx])
                acc +=cost 
            if l<=2:
                print(cand,nums)
            if acc<=k:
                k -=acc 
                ret += msk 
                for c, idx in cand:
                    if c == 0:
                        nums[idx] -=msk
                    if c ==msk- nums[idx]%msk:
                        
                        nums[idx] =nums[idx]+c -msk
                    else:
                        nums[idx] -= c + msk 
                    if l ==2:
                        print(c,msk,nums[idx]+c -msk,nums[idx],idx,nums)
            if ret >0:
                print(k,nums,ret)
        return ret






re =Solution().maximumAND(nums = [3,1,2], k = 8, m = 2)
print(re)