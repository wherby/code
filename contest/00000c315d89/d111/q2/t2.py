from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        m,n = len(str1),len(str2)
        idx = 0
        idx2 = 0
        def eqs(a,b):
            return a==b or ord(b) -ord(a) ==1 or (a=="z" and b=="a")
        while idx2<n:
            a = str2[idx2]
            while idx<m and not eqs(str1[idx],a):
                idx +=1
            #print(idx,idx2)
            if idx<m and eqs(str1[idx],a):
                idx +=1
                idx2 +=1
            if idx>=m:
                break
        #print(idx2,idx)
        return idx2 ==n and idx<=m




re =Solution().canMakeSubsequence(str1 = "abc", str2 = "ad")
print(re)