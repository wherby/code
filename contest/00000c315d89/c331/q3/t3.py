from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
import copy

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sll = [SortedList([]),SortedList([])]
        dicl = [{},{}]
        dicl[0][-1] =1
        for i,a in enumerate(nums):
            for j in range(2):
                if i-1 not in dicl[j]:
                    if len(sll[j])<k or (len(sll[j])==k and sll[j][-1]>a):
                        sll[j].add(a)
                        dicl[j][i] = 1
                        if len(sll[j]) >k:
                            sll[j].remove(sll[j][-1])
                            
        mx = 10**10
        for sl in sll:
            if len(sl)>0 and len(sl)==k:
                mx = min(mx,sl[-1])
        return mx 
        
                
                


#re =Solution().minCapability(nums = [2,3,5,9], k = 2)
#re =Solution().minCapability([4,22,11,14,25],3)
re = Solution().minCapability([24,1,55,46,4,61,21,52],3)
print(re)