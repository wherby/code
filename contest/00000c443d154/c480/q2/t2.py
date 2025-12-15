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
    def reverseWords(self, s: str) -> str:
        vowls=set(['a', 'e', 'i', 'o',  'u'])
        
        ls= s.split(" ")
        cur =len([a for a in ls[0] if a in vowls])
        ret = [ls[0]]
        for t1 in ls[1:]:
            c1 = len([a for a in t1 if a in vowls])
            #print(c1,cur)
            if c1 ==cur:
                ret.append(t1[::-1])
            else:
                ret.append(t1)

        return " ".join(ret)




re =Solution().reverseWords("sun one data")
print(re)