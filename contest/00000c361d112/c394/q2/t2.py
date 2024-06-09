from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

import string
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        cnt = 0
        atoz = list(string.ascii_lowercase)
        atoz2 = list(string.ascii_uppercase)
        dic = {}
        for i,a in enumerate( word):
            if a in atoz2 and  a not in dic:
                dic[a]=i
            if a in atoz:
                dic[a] =i
        for i,a in enumerate(atoz):
            if a in dic and atoz2[i] in dic and dic[a] < dic[atoz2[i]]:
                cnt +=1
        return cnt



re =Solution()
print(re)