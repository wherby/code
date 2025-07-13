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
    def processStr(self, s: str, k: int) -> str:
        
        acc = 0
        lst = len(s)
        for i,a in enumerate(s):
            if a.isalpha():
                acc +=1
            elif a == "*":
                if acc>0:
                    acc -=1
            elif a == "#":
                acc = acc*2 
            elif a =="%":
                acc = acc
        if k>= acc:
            return "."
        #print(acc)
        for a in s[::-1]:
            if a.isalpha():
                if k+1 == acc:
                    #print(k,acc,a)
                    return a
                acc -=1
            elif a =="*":
                acc +=1
            elif a == "#":
                if k >= acc //2:
                    k = k - acc//2
                acc = acc //2
            elif a=="%":
                k = acc-1 -k
            #print(a,k,acc)

a = "jio"+"#"+"*g"
print(a)
re = Solution().processStr(s = a, k = 1)
print(re) 
                
