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
    def kthDigit(self, k: int) -> int:
        l,r = 0,k
        
        def count(b):
            if b <0:
                return 0 
            if b ==0 :
                return 9
            total = 9
            
            mxd = len(str(10*b ))
            for d in range(2,mxd):
                t1 = 9*(10**(d-2))
                total += t1 *(10*d)
            start = 10**(mxd -2)
            cur=  b - start +1
            total += cur * (10*mxd)
            return total

        while l <r:
            md= (l+r)>>1
            if count(md) >=k:
                r=md 
            else:
                l = md +1
        
        prev = count(l-1)
        idx = k-prev -1
        num = ""
        if l ==0:
            return k
        if l %2 ==0:
            for i in range(10):
                num+= str(10*l + i)
        else:
            for i in range(9,-1,-1):
                num += str(10*l+i)
        return int(num[idx])
                





re =Solution()
print(re)