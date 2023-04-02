from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList

import math
class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        n = len(arr)
        m = math.gcd(n,k)
        k = m
        if n%k ==0:
            mid = n//k //2
            ls =[[] for _ in range(n)]
            for i,a in enumerate(arr):
                ls[i%k].append(a)
            for i in range(k):
                ls[i].sort()
            acc =0 
            for i in range(k):
                for a in ls[i]:
                    acc += abs(ls[i][mid] - a)
            return acc 
        else:
            arr.sort()
            mid = n //2 
            acc =0
            for a in arr:
                acc +=abs(arr[mid]-a)
            return acc
                





re =Solution().makeSubKSumEqual([6,2,8,5,7,10],4)
print(re)