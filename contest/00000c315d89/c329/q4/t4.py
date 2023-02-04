from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp= [10**10]*(n+1)
        dp[0] = 0 
        for i in range(n):
            dic =defaultdict(int)
            acc = 0
            for j in range(i,-1,-1):
                if dic[nums[j]] ==0:
                    acc +=1    
                elif dic[nums[j]] ==1:
                    acc -=1
                dic[nums[j]] +=1
                dp[i+1] = min(dp[i+1],dp[j]-acc+k)
        return dp[-1]+n



re =Solution().minCost(nums = [1,2,1,2,1,3,3], k = 2)
print(re)