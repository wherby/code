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
    def minimumGroups(self, words: List[str]) -> int:
        def getMin(s):
            n = len(s)
            ss = s+s 
            i,j,k = 0,1,0 
            while i <n and j <n and k<n:
                diff = ord(ss[i+k]) -ord(ss[j+k])
                if diff ==0:
                    k +=1
                else:
                    if diff>0:
                        i += k+1
                    else:
                        j +=k+1
                    if i == j:
                        j+=1
                    k = 0 
            start = min(i,j)
            return ss[start:start+n]
        dic = {}
        for w in words:
            eq= "".join([w[i] for i in range(0,len(w),2)])
            oq = "".join([w[i] for i in range(1,len(w),2)])
            eq = getMin(eq)
            oq = getMin(oq)
            dic[eq+oq] =1 
        return len(dic)





re =Solution()
print(re)