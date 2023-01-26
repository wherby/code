from typing import List, Tuple, Optional

import sys
sys.setrecursionlimit(10**4)
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
import math

class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        @cache
        def dfs(x,y):
            #print(x,y)
            if x ==1 or y ==1:
                return True
            if x %2 ==0:
                if dfs(x//2,y): 
                    return True
            elif y %2 ==0:
                if dfs(x,y//2): return True
            elif x>y:
                if dfs(x-y,y):return True
            elif x <y:
                if dfs(x,y-x):return True
            return False
        return dfs(targetX,targetY)

re =Solution().isReachable(900000000,3)
print(re)