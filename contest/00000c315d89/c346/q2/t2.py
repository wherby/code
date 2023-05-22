from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        n = len(s)
        ls = [a for a in s]
        for i in range(n//2):
            if ls[i] != ls[n-1-i]:
                if ls[i] > ls[n-1-i]:
                    ls[i]=ls[n-1-i]
                else:
                    ls[n-1-i] = ls[i]
        return "".join(ls)




re =Solution().makeSmallestPalindrome("egcfe")
print(re)