from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        n = len(parent)
        @cache
        def getVals(idx):
            if idx ==0:return 0
            return getVals(parent[idx]) ^(1<< (ord(s[idx])-ord('a')))
        vals = [getVals(i) for i in range(n)]
        dic = defaultdict(int)
        sm = 0 
        for x in vals:
            sm += dic[x]
            for i in range(26):
                sm +=dic[x ^(1<<i)]
            dic[x] +=1
        return sm



re =Solution().countPalindromePaths(parent = [-1,0,0,1,1,2], s = "acaabc")
print(re)