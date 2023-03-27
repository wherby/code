from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        
        def dfs(idx):
            #print(state)
            if idx ==n:
                if len(state)>0:
                    return 1
                else:
                    return 0 
            res =0
            if nums[idx]-k not in state:
                state[nums[idx]] =1
                res +=dfs(idx+1)
                del state[nums[idx]]
            res +=dfs(idx+1)
            return res
        state={}
        return dfs(0)
                




re =Solution().beautifulSubsets([10,4,5,7,2,1],3)
#re =Solution().beautifulSubsets(nums = [2,4,6], k = 2)
#re =Solution().beautifulSubsets([1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000],1)
print(re)