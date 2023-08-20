from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        res=[]
        dic={}
        for i in range(1,200):
            if len(res) == n:
                return sum(res)
            if i not in dic:
                res.append(i)
                dic[k-i] =1
        





re =Solution().minimumSum(5,4)
print(re)