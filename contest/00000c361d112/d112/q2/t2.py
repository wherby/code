from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s11= [a for i,a in enumerate(s1) if i %2==0]
        s12= [a for i,a in enumerate(s1) if i %2==1]
        s21= [a for i,a in enumerate(s2) if i %2==0]
        s22= [a for i,a in enumerate(s2) if i %2==1]
        #@print(s11,s21,s11.sort(),s11.sort()==s21.sort())
        s11.sort()
        s12.sort()
        s21.sort()
        s22.sort()
        return s11==s21 and s12 ==s22
        




re =Solution().checkStrings(s1 = "abe", s2 = "bea")
print(re)