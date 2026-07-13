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
    def minOperations(self, s1: str, s2: str) -> int:
        n = len(s1)
        cur = 0 
        s1 = [a for a in s1]
        for i in range(n):
            if s1[i] == "0" and s2[i]=="1":
                cur +=1
                s1[i]= "1" 
                continue
            elif s1[i] =="1" and s2[i] == "0":
                if i < n-1 and s1[i+1] == "1":
                    s1[i+1] = "0"
                    cur +=1 
                    continue
                if i <n-1 and s1[i+1] == "0":
                    cur +=2
                    continue
                if i >0 and s1[i-1]=="1":
                    cur +=2
                    continue 
                if i >0 and s1[i-1] == "0":
                    cur +=2 
                    continue 
                return -1
            elif s1[i] == s2[i]:
                continue
            else:
                return -1
        return cur 





re =Solution().minOperations(s1 = "10", s2 = "00")
print(re)