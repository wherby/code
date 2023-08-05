from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
from itertools import pairwise
class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        n = len(nums)
        nums = nums+nums
        dic = defaultdict(list)
        for i,a in enumerate(nums):
            dic[a].append(i)
        mx = n 
        for _,ls in dic.items():
            tp = 0
            for a,b in pairwise(ls):
                tp = max(tp,(b-a)//2)
            mx = min(mx,tp)
        return mx




re =Solution().minimumSeconds(nums = [1,2,1,2])
print(re)