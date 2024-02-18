from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        ret = [0]*n 
        for i in range(n):
            ret[i] = (n-1-i)*2
        if x == y or abs(x-y) ==1:
            return ret
        
        if x > y:
            x,y = y,x
        ret = [0]*n
        m = n - (y-x-1)
        if m >2:
            for i in range(m):
                ret[i] = (m-1-i) *2
        #print(ret,m)
        cir = (y-x-1)
        cir2 = (y-x+1)
        left,right = cir//2, cir - cir//2
        for i in range(cir2//2):
            if i != cir2//2-1:
                ret[i] += cir2*2
            else:
                ret[i] = cir2
        #print(ret,cir)
        #ret[0] -=2
        
        l1 = left +x
        #print(ret)
        def f1(leftCir,left):
            m = leftCir + left
            for i in range(m):
                ret[i] += (m-1-i)*2
            for i in range(leftCir):
                ret[i] -=(leftCir-1-i)*2
            for i in range(left):
                ret[i] -= (left -1-i) *2
        
        #print(ret)
        #print(left,x,right)
        #print(right,n-y+1)
        if (y-x)%2 == 0:
            f1(left,x)
            f1(right,n-y+1)
            f1(left,n-y+2)
            f1(right,x)
            #ret[0]=2
        else:
            f1(left,x)
            f1(right,n-y+1)
            f1(left,n-y+2)
            f1(right,x+1)
        return ret






re =Solution().countOfPairs(n = 4, x = 1, y = 4)
print(re)