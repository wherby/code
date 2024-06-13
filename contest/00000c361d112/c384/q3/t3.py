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
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        c =Counter()
        for w in words:
            c1 = Counter(w)
            c +=c1 
        ls = []
        for w in words:
            ls.append(len(w))
        ls.sort()
        vs = list(c.values())
        ret =0
        o,e = 0,0
        for a in vs:
            if a%2==0:
                e +=a//2
            else:
                e += a //2 
                o +=1
        for a in ls:
            if a %2 ==0 and e >=a //2:
                e -= a //2 
                ret +=1
            elif e >= a //2:
                e -= a //2 
                ret +=1
        return ret
        





re =Solution().maxPalindromesAfterOperations(["abc","ab"])
print(re)