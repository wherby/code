from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        n = 64
        ls = [num1]*n
        
        for i in range(n):
            ls[i] = ls[i] - num2*i
        #print(ls)
        mx = 65
        for i in range(1,64):
            if ls[i]<i:continue
            a = bin(ls[i]).count("1")
            if a <=i :
                return i 
        return -1





re =Solution().makeTheIntegerZero(num1 = 110, num2 = 55)
print(re)