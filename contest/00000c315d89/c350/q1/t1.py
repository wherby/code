from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue


class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        res = 0
        while mainTank >=5:
            if additionalTank>0:
                mainTank +=1
                additionalTank-=1
                res +=5
                mainTank -=5
            else:
                res +=5
                mainTank -=5
        res += mainTank
        return res*10





re =Solution().distanceTraveled(5,10)
print(re)