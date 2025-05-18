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
    def minSwaps(self, nums: List[int]) -> int:
        ls =[(a,i ) for i,a in enumerate(nums)]
        ls.sort(key= lambda x: (sum([int(a) for a in str(x[0]) ]),x[0]))
        cnt = 0
        n = len(nums)
        for i in range(n):
            cur =i
            while i != ls[i][1]:
                t = ls[cur][1]
                ls[t],ls[i] = ls[i],ls[t]
                cnt +=1
        return cnt




re =Solution().minSwaps([346675656,436516098,372126778,781771807])
print(re)