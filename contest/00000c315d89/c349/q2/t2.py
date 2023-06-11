from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
class Solution:
    def smallestString(self, s: str) -> str:
        n = len(s)
        start,end = 0,0 
        for i,a in enumerate(s):
            if a != "a":
                break
            else:
                start = i+1
        end = start
        for j in range(start,n):
            if s[j] == "a":
                break
            else:
                end = j+1
        #print(start,end)
        if start == end:
            return s[:start-1] + "z"
        replace = ""
        for i in range(start,end):
            replace += chr(ord(s[i]) -1)
        ret = s[:start] + replace + s[end:]
        return ret





re =Solution().smallestString("leetcode")
print(re)