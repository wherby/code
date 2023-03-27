from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        cnt= 0
        st =[]
        for a in nums:
            heapq.heappush(st,a)
        while st:
            while st and st[0]<=nums[cnt]:
                heapq.heappop(st)
            if st:
                cnt +=1
                heapq.heappop(st)
        return cnt
        




re =Solution().maximizeGreatness( [1,3,5,2,1,3,1])
print(re)