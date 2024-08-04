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
    def numberOfSubstrings(self, s: str) -> int:

        zeros = [-1]

        sm = 0
        for i,a in enumerate(s):
            if a =="0":
                zeros.append(i)
            sm += i-zeros[-1]
            m = max(0,len(zeros)-201)
            
            for j,a in enumerate(reversed(zeros[m+1:])):
                #print(j,a,"aaaaa",i)
                if (j+1)**2 + (j+1) <=(i-a+1):
                    sm += a - zeros[-j-2]
                    #print("nb",i,i-a+1,j)
                else:
                    sm +=max(0, i- zeros[-j-2] -(j+1)**2-j)
                    #print("c",sm,i- zeros[-j-2])
            #print(i,sm,zeros)
            
            
        return sm 
            





re =Solution().numberOfSubstrings("101101")
print(re)