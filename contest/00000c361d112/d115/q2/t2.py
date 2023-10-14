from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        ret = []
        lastG = -1
        for w,g in zip(words,groups):
            if g != lastG:
                ret.append(w)
                lastG =g 
        return ret





re =Solution()
print(re)