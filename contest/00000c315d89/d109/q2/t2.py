from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
class Solution:
    def sortVowels(self, s: str) -> str:
        vos = ['a', 'e', 'i', 'o',  'u']
        n = len(s)
        ret = [""]*n
        cc = []
        for i,a in enumerate(s):
            if a.lower() not in vos:
                ret[i] =a
            else:
                cc.append(a)
        cc.sort(reverse= True)
        for i in range(n):
            if ret[i] == "":
                ret[i]= cc.pop()
        return "".join(ret)





re =Solution()
print(re)