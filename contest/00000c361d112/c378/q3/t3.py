from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def maximumLength(self, s: str) -> int:
        mx = -1
        n = len(s)
        start = 0 
        idx = 0
        dic = defaultdict(int)
        lls = [[] for _ in range(26)]
        while idx < n:

            if s[idx] != s[start]:
                l = idx-start
                lls[ord(s[start]) - ord('a')].append(l)
                start = idx
            idx +=1
        l = idx-start 
        lls[ord(s[start]) - ord('a')].append(l)
        for i in range(26):
            ls = lls[i].sort()
            if len(ls) >0 and  ls[-1] > 2:
                mx = max(mx,ls[-1] -1)
            if len(ls) >1 :
                mx = max(mx,ls[-2])
        #print(dic)
            #print(idx,start)
        return mx
                





re =Solution().maximumLength("iiiiifffffffoooookkkfffffffnnxxxxxx")
print(re)