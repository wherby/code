from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList


class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        mx = 0 
        n = len(word)
        dic ={}
        for f in forbidden:
            dic[f] = 1
        left=0
        def verify(i):
            ls = word[left:i+1][-10:]
            m = len(ls)
            for i in range(m):
                if ls[i:] in dic:
                    return False
            return True
        for i,a in enumerate(word):
            while not verify(i):
                left +=1
            mx = max(mx,i+1-left)
        return mx




re =Solution().longestValidSubstring(word = "cbaaaabc", forbidden = ["aaa","cb"])
print(re)