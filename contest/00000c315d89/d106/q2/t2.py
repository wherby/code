from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        def verify(s):
            cnt = 0
            for i in range(len(s)-1):
                if s[i] == s[i+1]:
                    cnt +=1
            return cnt <=1
        n = len(s)
        mx =1
        for le in range(1,n+1):
            for j in range(n-le+1):
                s1 = s[j:j+le]
                if verify(s1):
                    mx = max(mx,le)
        return mx



re =Solution()
print(re)