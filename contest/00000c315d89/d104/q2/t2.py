from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        m,n  = len(nums),len(nums[0])
        cnt = 0 
        nums= [sorted(a) for a in nums]
        for i in range(n):
            mx =0
            for j in range(m):
                mx = max(mx,nums[j][i])
            cnt += mx 
        return cnt




re =Solution().matrixSum([[7,2,1],[6,4,2],[6,5,3],[3,2,1]])
print(re)