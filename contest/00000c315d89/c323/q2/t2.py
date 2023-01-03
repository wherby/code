from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        ret = -1
        pre = 0
        acc =0
        nums.sort(reverse=True)
        dic =defaultdict(int)
        for a in nums:
            if a*a in dic:
                k = dic[a*a]+1
                dic[a] = max(dic[a],k)
                if k>=2:
                    ret = max(ret,k)
            else:
                dic[a] =1
        return ret




re =Solution().longestSquareStreak([4,3,6,16,8,2])
print(re)