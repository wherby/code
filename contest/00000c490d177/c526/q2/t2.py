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
    def minimumMaxValue(self, n: int, index: int, value: int) -> int:
        ls = [-1]*n
        ls[index]= value
        m = min(10**5+5,(value+value)//(index+1))+100
        lstP = value
        for i in range(2,m):
            if value %i ==0:
                lstP =i 
                break 
        if lstP ==1:
            return -1
        
        if (value-lstP)//2   < index:
            return -1 
        if index == n-1:
            return value
        
        ret = value + lstP * (n-index-1)
        value = value +lstP
        #print(ret)
        ret= min(ret,value + 2*(n-index-2))
        #print(value,ret,lstP)
        return ret






re =Solution().minimumMaxValue(42,14,39)
print(re)