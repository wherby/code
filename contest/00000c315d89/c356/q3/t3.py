from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

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
        res.append(merge(a,merge(b,c)))
        res.append(merge(a,merge(c,b)))
        res.append(merge(b,merge(a,c)))
        res.append(merge(b,merge(c,a)))
        res.append(merge(c,merge(a,b)))
        res.append(merge(c,merge(b,a)))
        res.append(merge(merge(b,c),a))
        res.append(merge(merge(c,b),a))
        res.append(merge(merge(a,c),b))
        res.append(merge(merge(c,a),b))
        res.append(merge(merge(a,b),c))
        res.append(merge(merge(b,a),c))
        res.sort(key=lambda x:(len(x),x))
        #print(res)
        return res[0]




re =Solution().minimumString("aba","c","b")
print(re)