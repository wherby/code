from typing import List, Tuple, Optional

from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
import math

class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        isR = False
        
        while True:
            px,py = targetX,targetY
            if targetX ==1 or targetY ==1:
                isR = True
                break
            if targetX %2 ==0 : 
                targetX = targetX //2
                continue
            if targetY %2 ==0 : 
                targetY = targetY //2 
                continue
            if targetX> targetY: 
                targetX = targetX -targetY
                continue
            if targetY > targetX: 
                targetY=targetY - targetX
                continue
            if targetY ==px and targetY == py:
                break
        return isR

re =Solution().isReachable(900000000,3)
print(re)