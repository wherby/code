from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        dic = {}
        acc =0
        cnt = 0
        idx = 0 
        for i in range(1,3*n+1):
            if cnt == n:
                return acc 
            if i not in dic:
                acc +=i 
                cnt +=1
                dic[target-i] =1
        





re =Solution().minimumPossibleSum(2,3)
print(re)