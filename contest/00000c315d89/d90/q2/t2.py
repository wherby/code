from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def cnt(a,b):
            c = 0
            n = len(a)
            for i in range(n):
                if a[i]!=b[i]:
                    c +=1
            return c 
        ret=[]
        for a in queries:
            fd = False
            for b in dictionary:
                if cnt(a,b)<=2:
                    fd = True
            if fd ==True:
                ret.append(a)
        return ret





re =Solution()
print(re)