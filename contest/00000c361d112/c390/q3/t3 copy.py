from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf


        
class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        ret= []
        sl = SortedList()
        dic ={}
        for i,a in enumerate(freq):
            if nums[i] not in dic:
                dic[nums[i]]=(a,nums[i])
                sl.add((a,nums[i]))
            else:
                c,d = dic[nums[i]]
                cn = c +a 
                dic[nums[i]] = (cn,d)
                sl.remove((c,d))
                sl.add((cn,d))
            ret.append(sl[-1][0])
        return ret






re =Solution().mostFrequentIDs(nums = [2,3,2,1], freq = [3,2,-3,1])
print(re)