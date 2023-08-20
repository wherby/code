from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import functools


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        m,n = len(str1),len(str2)
        acc =0 
        def eqs(a,b):
            return a==b or ord(b) -ord(a) ==1 or (a=="z" and b=="a")
        idx = 0
        for a in str2:
            while idx< m and not eqs(str1[idx],a):
                idx +=1
            if idx<m and eqs(str1[idx],a):
                idx +=1
                acc +=1
            #print(a,idx,acc)
        #print(acc,a)
        return acc ==n




re =Solution().canMakeSubsequence(str1 = "abc", str2 = "ad")
print(re)