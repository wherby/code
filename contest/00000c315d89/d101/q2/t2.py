from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        dic = {}
        for i in range(26):
            a = chr(ord('a')+i) 
            dic[a] = i+1
        for i,a in enumerate(chars):
            dic[a] = vals[i]
        mx = 0
        acc =0 
        for a in s:
            acc += dic[a]
            if acc<0:
                acc =0 
            mx = max(mx,acc)
        return mx
            




re =Solution().maximumCostSubstring(s = "adaa", chars = "d", vals = [-1000])
print(re)