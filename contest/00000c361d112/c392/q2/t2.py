from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        ABC = 'abcdefghijklmnopqrstuvwxyz'
        dic ={}
        for i,a in enumerate(ABC):
            dic[a]  =i 
        #print(dic)
        ret = ""
        for a in s:
            mx = min(dic[a]-dic['a'],26-dic[a])
            t = min(k,mx)
            ft = min(dic[a]-t, (dic[a] +t)%26)
            ret += ABC[ft]
            k -= t
        return ret



re =Solution().getSmallestString(s = "zbbz", k = 3)
print(re)