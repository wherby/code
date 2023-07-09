from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        dic = defaultdict(int)
        for a in nums:
            dic[a] +=1
        for f,t in zip(moveFrom,moveTo):
            a = dic[f]
            del dic[f]
            dic[t] +=a 
        ls =list(dic.keys())
        ls.sort()
        return ls




re =Solution()
print(re)