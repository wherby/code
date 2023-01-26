from typing import List, Tuple, Optional
# https://leetcode.cn/problems/check-if-point-is-reachable/solution/qiu-chu-lu-jing-by-981377660lmt-5dbh/

from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
import math

class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        return math.gcd(targetX,targetY).bit_count()==1
    
    def findPath(self, targetX: int, targetY: int) ->  List[Tuple[int, int]]:
        if not self.isReachable(targetX,targetY):
            return []
        path = []
        while (targetX,targetY) != (1,1):
            path.append((targetX,targetY))
            if targetX %2 ==0:
                targetX = targetX //2
                continue
            if targetY %2 ==0:
                targetY = targetY //2
                continue
            if targetX > targetY:
                targetX -= targetY
            else:
                targetY -= targetX
        path.append((1,1))
        return path[::-1]

re =Solution().findPath(4,7)
print(re)