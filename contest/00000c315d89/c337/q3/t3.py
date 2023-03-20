from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        cnt =0 
        def verify(state):
            dic= {}
            for i in range(n):
                if (1<<i) &state:
                    y = nums[i]
                    if y-k in dic:return False
                    dic[y] =1
            return True
        for i in range(1,1<<n):
            #print(i,n)
            if verify(i):
                cnt +=1
        return cnt





re =Solution().beautifulSubsets([10,4,5,7,2,1],3)
#re =Solution().beautifulSubsets(nums = [2,4,6], k = 2)
print(re)