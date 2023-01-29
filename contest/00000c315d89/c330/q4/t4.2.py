from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

 
        
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        
        n = len(nums)
        mx1 = [[0]*n for _ in range(n)]
        mx2 = [[0]*n for _ in range(n)]
        for j in range(1,n):
            acc = len([i for i in range(j+1,n) if nums[j] < nums[i]])
            for k in range(j+1,n-1):
                if nums[j]> nums[k]:
                    mx1[j][k] = acc 
                else:
                    acc -=1
        for k in range(2,n):
            acc = len([i for i in range(k) if nums[i]< nums[k]])
            for j in range(k-1,0,-1):
                if nums[j]> nums[k]:
                    mx2[j][k] =acc 
                else:
                    acc -=1
        sm = 0 
        for j in range(1,n-2):
            for k in range(j+1,n-1):
                sm += mx1[j][k] * mx2[j][k]
        #print(mx1,mx2)
        return sm




re =Solution().countQuadruplets([1,3,2,4,5])
#re =Solution().countQuadruplets([2,5,3,1,4])
print(re)