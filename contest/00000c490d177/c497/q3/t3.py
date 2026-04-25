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
from collections import Counter
class Solution:
    def longestBalanced(self, s: str) -> int:
        c = Counter(s)
        if c["0"]==0 or c["1"] ==0:
            return 0
        dic={}
        dic[0] = -1 
        cur = 0 
        ret = 0 
        for i,a in enumerate(s):
            cur +=1 if a =="1" else -1 
            for diff in [0,2,-2]:
                target = cur -diff 
                
                if target in dic:
                    j = dic[target]
                    l = i-j 
                    ones = (l+diff)//2
                    zeros = l-ones
                    if diff ==0:
                        ret = max(ret,l)
                    elif diff ==2 and c["0"]>zeros:
                        ret = max(ret,l)
                    elif diff== -2 and c["1"]>ones:
                        ret = max(ret,l)
            if cur not in dic:
                dic[cur] = i 
        print(dic)
        return ret







re =Solution().longestBalanced("01111100")
print(re)