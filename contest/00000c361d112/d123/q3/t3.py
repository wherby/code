from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
#from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        pre = [0]
        for a in nums:
            pre.append(pre[-1] +a)
        dic ={}
        ret = -10**19
        for i,a in enumerate(nums):
            if a+k in dic:
                ret = max(ret, pre[i+1]-pre[dic[a+k]-1])
            if a-k in dic:
                ret = max(ret,pre[i+1]- pre[dic[a-k]-1])
            if a not in dic:
                dic[a] = i+1
            else:
                if pre[i+1]< pre[dic[a]]:
                    dic[a] = i+1
            #print(dic)
        return ret if ret != -10**19 else 0






re =Solution().maximumSubarraySum(nums = [-1,-2,-3,-4], k = 2)
print(re)