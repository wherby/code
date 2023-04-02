from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        ls =[]
        n = len(reward1)
        for i,a in enumerate(reward1):
            ls.append((a- reward2[i],i))
        ls.sort(reverse=True)
        acc =0
        dic ={}
        for i in range(k):
            _,idx = ls[i]
            acc += reward1[idx]   
            dic[idx] =1
        for i in range(n):
            if i in dic:continue
            acc += reward2[i]
        return acc





re =Solution()
print(re)