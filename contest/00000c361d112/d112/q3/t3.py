from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        n = len(nums)
        mx = 0
        acc =0
        dic= defaultdict(int)
        for i in range(n):
            dic[nums[i]] +=1
            acc += nums[i]
            if i >=k:
                b = nums[i-k]
                acc -= nums[i-k]
                dic[b] -=1
                if dic[b] ==0:
                    del dic[b]
            #print(i,dic,len(dic),k)
            if len(dic) >= m:
                #print(i,acc,dic)
                mx = max(mx,acc)
        return mx




re =Solution().maxSum(nums = [2,6,7,3,1,7], m = 3, k = 4)
print(re)