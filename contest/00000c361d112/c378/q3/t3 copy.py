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
        lsm = [0]*26
        def getMx(a,l):
            nonlocal mx
            k = ord(a) - ord('a')
            
            if l >2:
                mx = max(mx,l-2)
            if lsm[k]>l:
                mx = max(mx,l)
            if (a,l-1) in dic:
                mx = max(mx,l-1)
            if dic[(a,l)] >0 and l >1:
                mx =max(mx,l-1)
            if dic[(a,l)] >1:
                mx = max(mx,l)
            lsm[k] = max(lsm[k],l)
            #print(k,lsm,mx,dic,l)

        
        while idx < n:

            if s[idx] != s[start]:
                l = idx-start
                getMx(s[start],l)
                dic[(s[start],l)] +=1
                start = idx
            idx +=1
        l = idx-start 
        
        getMx(s[start],l)
        dic[(s[start],l)] +=1
        #print(dic)
            #print(idx,start)
        return mx
                





#re =Solution().maximumLength("iiiiifffffffoooookkkfffffffnnxxxxxx")
re =Solution().maximumLength("jicja")
print(re)