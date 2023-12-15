from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
import math
INF  = math.inf

class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort(reverse=True)
        cnt =0
        acc =0
        nxt = 1
        while nxt <=target:
            while coins and coins[-1]  <=nxt:
                a = coins.pop()
                acc +=a 
            if acc >=nxt:
                pass
            else:
                acc += acc+1
                cnt +=1
            nxt +=1
        return cnt




re =Solution().minimumAddedCoins(coins = [1,4,10], target = 19)
print(re)