from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf

class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        def findMax(nums,start):
            ans = -10**10
            min_pre,pre_sum = 0,0
            s1 = start
            ret =[s1,s1]
            for i,a in enumerate(nums,start):
                pre_sum += a 
                if ans <pre_sum-min_pre:
                    ans = pre_sum-min_pre
                    ret = [s1,i]
                if min_pre > pre_sum:
                    min_pre =pre_sum
                    s1=i+1
            #print(nums,start,ret,s1,pre_sum,min_pre)
            return ret
        sm = 0
        idx = 0
        while k:
            if k%2 ==1:
                ls =nums[idx:n-k+1]
                st,end = findMax(ls,idx)
                sm += k *sum(nums[st:end+1])
                idx = end+1
            else:
                ls = nums[idx:n-k+1]
                ls = [-a for a in ls]
                st,end = findMax(ls,idx)
                sm -= k*sum(nums[st:end+1])
                idx = end+1
            k -=1
            #print(sm,st,end)
        return sm
        
        




re =Solution().maximumStrength([3,-87,21,-86,44,-36,80],5)
print(re)