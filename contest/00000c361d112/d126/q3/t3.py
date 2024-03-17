from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

from collections import Counter
class Solution:
    def minimizeStringValue(self, s: str) -> str:
        ls = [0]*26
        ret =[]
        #print(st)
        ABC='abcdefghijklmnopqrstuvwxyz'
        for a in s:
            if a != "?":
                ls[ord(a) - ord('a')] +=1
            else:
                mn = min(ls)
                for i in range(26):
                    if ls[i] == mn:
                        ls[i]+=1
                        ret.append(ABC[i])
                        break
        #print(ret)
        ret.sort()
        i=0
        res =[]
        for a in s:
            if a =="?":
                res.append(ret[i])
                i+=1
            else:
                res.append(a)
        return "".join(res)




re =Solution().minimizeStringValue( s = "abcdefghijklmnopqrstuvwxy??")
print(re)