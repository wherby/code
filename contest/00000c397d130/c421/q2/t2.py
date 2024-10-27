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
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9+7
        ls= [0]*26
        for a in s:
            ls[ord(a) - ord('a')] +=1
        
        tls= []
        for i in range(26):
            tmp = [0]*26
            tmp[i] =1 
            for j in range(26):
                t1 = [0]*26
                for k in range(25):
                    t1[k+1] += tmp[k]
                t1[0] += tmp[-1]
                t1[1] += tmp[-1]
                tmp =t1 
            tls.append(tmp)
        x,y = t //26,t%26
        for _ in range(x):
            t1 = [0]*26
            for i in range(26):
                t2 = [a* ls[i] for a in tls[i]]
                t1 =[a+b for a,b in zip(t2,t1)]
            ls= t1
        for _ in range(y):
            t1 = [0]*26
            for k in range(25):
                    t1[k+1] += ls[k]
            t1[0] += ls[-1]
            t1[1] += ls[-1]
            ls =t1
        return sum(ls)

        





re =Solution().lengthAfterTransformations( s = "abcyy", t = 5000)
print(re)