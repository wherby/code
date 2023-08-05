from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 

from sortedcontainers import SortedDict,SortedList
import itertools
class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        def merge(a,b):
            #print(a,b)
            m,n= len(a),len(b)
            for i in range(m+1):
                if a[i:] == b[:min(m-i,n)] :
                    return a[:i]+b 
                elif  a[i:i+n] ==b:
                    return a
        #print(merge(a,b),a,b)
        res = []
        idxs = [a,b,c]
        ls = itertools.permutations(idxs)
        for x,y,z in ls:
            #print(x,y,z)
            res.append(merge(x,merge(y,z)))
            res.append(merge(merge(y,z),x))
        res.sort(key=lambda x:(len(x),x))
        return res[0]




re =Solution().minimumString("aba","c","b")
print(re)