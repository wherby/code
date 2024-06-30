from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf

class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        cnt,cnt2= 0,0
        ls= [red,blue]
        ls2 = ls[::-1]
        while cnt < ls[cnt %2] :
            ls[cnt%2]-=cnt+1
            cnt +=1
        while cnt2 < ls2[cnt2 %2] :
            ls2[cnt2%2]-=cnt2+1
            cnt2 +=1
        return max(cnt,cnt2)





re =Solution().maxHeightOfTriangle( red = 2, blue = 4)
print(re)